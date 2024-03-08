from tqdm import tqdm
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import time

from utility import get_html


def get_flows(html: bytes, args: dict) -> pd.DataFrame:
    '''
        Парсинг страницы с потоками https://journal.tinkoff.ru/flows/
        Собирает: названия потоков, топики потоков, ссылки на страницы топиков
    '''
    flow_dict = {'flow_title': [], 'start_topic': [], 'flow_link': []}
    if html is None:
        return pd.DataFrame(flow_dict)
    soup = bs(html,'html.parser')
    items = soup.find_all(**(args['flow_inner_args']))[:args['flows_cards_num']]
    print(f'Всего flows: {len(items)}')
    
    for item in tqdm(items):
        flow_items = item.find_all(**(args['flow_topic_args']))[:args['flows_units_per_card']]
        
        for flow_item in flow_items:
            flow_dict['start_topic'].append(flow_item.text)
            flow_link = f"https://journal.tinkoff.ru{flow_item.get('href')}"
            # не во всех потоках есть posts
            if get_html(f'{flow_link}posts/').status_code == 200:
                flow_dict['flow_link'].append(f'{flow_link}posts/')
            else:
                flow_dict['flow_link'].append(flow_link)

        flow_dict['flow_title'] += [item.find(**(args['flow_title_args'])).text] * len(flow_items)
    return pd.DataFrame(flow_dict)


def get_flow_page_news(html: bytes, args: dict, links_visited: set) -> pd.DataFrame:
  '''
    Парсинг страницы потока
  '''
  soup = bs(html,'html.parser')
  items = soup.find_all(**(args['article_card_args']))[:args['news_per_page']] # поиск всех карточек с новостями
  news_dict = {'author': [], 'date': [], 'views': [],
                  'topic': [], 'title': [], 'link': [],
                'likes':[], 'comments_count':[], 'saves_count': []}
    
  print(f'Новостей на странице: {len(items)}')
  bad_items = []
  skipped_news_count = 0
  for item in tqdm(items):
    
    try:
      article_link = 'https://journal.tinkoff.ru' + item.find(**(args['article_link_args'])).get('href')
      if article_link not in links_visited:
        links_visited.add(article_link)
        news_dict['author'].append(item.find(**(args['article_author_args'])).text)
        news_dict['date'].append(item.find(**(args['article_date_args'])).get('datetime'))
        news_dict['views'].append(item.find(**(args['article_views_args'])).text)
        news_dict['title'].append(item.find(**(args['article_title_args'])).text)
        news_dict['link'].append(article_link)
        news_dict['likes'].append(item.find(**(args['article_likes_args'])).text)
        news_dict['comments_count'].append(item.find(**(args['article_comments_count_args'])).text)
        news_dict['saves_count'].append(item.find(**(args['article_saves_count_args'])).text)
      else:
        skipped_news_count += 1
        continue

    except Exception:
        skipped_news_count += 1
        bad_items.append(item)
        continue
  news_dict['topic'] = [soup.find(**(args['topic_args'])).text] * (len(items) - skipped_news_count)
  return pd.DataFrame(news_dict), bad_items


def parse_flow(flow_link: str, args, links_visited: set):
    '''
        По главной ссылке на поток проход по всем её страницам
    '''
    flow_df = pd.DataFrame({'author': [], 'date': [], 'views': [],
                            'topic': [], 'title': [], 'link': [],
                            'likes':[], 'comments_count':[], 'saves_count': [], 'flow_page_link': [], 'flow_link': []})
    for page in tqdm(range(1, args['nums_pages'] + 1)):
        print('Парсинг страничек')
        time.sleep(3)
        try:
            page_link = f'{flow_link}page/{page}'
            html = get_html(page_link).content
            # получение данных о новостных карточках на странице
            flow_page_df, bad_items = get_flow_page_news(html, args, links_visited)
            flow_page_df['flow_page_link'] = [page_link]*flow_page_df.shape[0]
            flow_page_df['flow_link'] = [flow_link]*flow_page_df.shape[0]
            flow_df = pd.concat([flow_df, flow_page_df], ignore_index=True)
            
        except Exception:
            continue

    return flow_df


def parse_flows(flows_links: np.ndarray, args):
    '''
        Парсинг страниц потоков по их ссылкам
    '''
    flows_df = pd.DataFrame({'author': [], 'date': [], 'views': [],
                            'topic': [], 'title': [], 'link': [],
                            'likes':[], 'comments_count':[], 'saves_count': [],
                            'flow_page_link': [], 'flow_link': []})
    links_visited = set() #Множество ссылок на новости которые уже добавили
    
    for flow_link in tqdm(flows_links):
        print(len(links_visited))
        print('парсинг потока')
        try:

            flow_df = parse_flow(flow_link, args, links_visited)
            flows_df = pd.concat([flows_df, flow_df], ignore_index=True)
            
        except Exception:
            continue
    return flows_df


def get_article_content(link: str):
    '''
        link - полная ссылка на конкретную новость
    '''
    try:
        html = get_html(link).content
        soup = bs(html,'html.parser')
        article_text = soup.find('div', attrs = {'class':'_articleView_1v9h1_1'}).text
        article_author = soup.find(lambda tag: (tag.name == 'a' or tag.name == 'div')\
                                and tag.get('class') == ['_author_1qoqa_6']).text
        topic_name = soup.find('a', attrs = {'class':'_flow_1xwjy_45'}).text
        return [article_text.replace(article_author, ''), topic_name]
    except:
        return [None, None]


def get_articles_content(article_links: np.array) -> pd.DataFrame:
    '''
        article_links - все ссылки на новостные статьи
        topic_name новости может не совподать с топиком потока(start_topic)
    '''
    articles_contens = [] 
    for article_link in article_links:
        t = get_article_content(article_link)
        t.append(article_link)
        articles_contens.append(t)
    return pd.DataFrame(articles_contens, columns=['article_text', 'topic_name', 'link'])