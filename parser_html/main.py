import requests as rq
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from tqdm import tqdm
import numpy as np
from fake_useragent import UserAgent

from utility import get_html

from parser_funcs import get_flows, get_flow_page_news, parse_flow, parse_flows, get_article_content, get_articles_content, get_article_content, get_articles_content



FILE = '../tinkoffjournal.csv'

get_flows_args = {'flow_inner_args': {'name': 'div', 'attrs': {'class': 'inner--q56lc'}},
                  'flow_topic_args': {'name':'a', 'attrs': {'class': 'item--gPa1X'}},
                  'flow_title_args': {'name': 'h4','attrs': {'class': 'heading--NuQf6'}},
                  'flows_cards_num' : 2, 'flows_units_per_card': 1
                  }

get_flow_news_args = {'article_card_args': {'name': 'div', 'attrs': {'class': 'card--VPII2'}},
                      'article_link_args': {'name': 'a', 'attrs': {'class': 'link--ILico'}},
                      'article_author_args': {'name': 'div', 'attrs': {'class': 'name--T02LD'}},
                      'article_date_args': {'name': 'time', 'attrs': {'class':'date--lnCxF'}},
                      'article_views_args': {'name': 'span', 'attrs': {'class': 'counter--JuiF0'}},
                      'article_title_args': {'name': 'h3', 'attrs': {'class': 'title--K0VOg'}},
                      'article_likes_args': {'name': 'button', 'attrs': {'class': 'likes--nMe0e'}},
                      'article_comments_count_args': {'name': 'a', 'attrs': {'class': 'bubble--H_faa'}},
                      'article_saves_count_args': {'name': 'button', 'attrs': {'class': 'favorites--P_JlB'}},
                      'topic_args': {'name': 'h1', 'attrs': {'class': 'heading--NuQf6'}},
                      'news_per_page': 2, 'nums_pages': 1
                      }

flows_page_link = "https://journal.tinkoff.ru/flows/"


html = get_html(flows_page_link).content
flow_df = get_flows(html, get_flows_args)
flows_cards_df = parse_flows(flow_df['flow_link'].values, get_flow_news_args)
articles_content_df = get_articles_content(flows_cards_df['link'].values)
merged_df = flows_cards_df.merge(articles_content_df, on='link', how='left')
final_df = flow_df.merge(merged_df, on='flow_link', how='left')
print(final_df)
final_df.to_csv(FILE)