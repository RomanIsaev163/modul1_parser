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

get_flows_args = {'flow_inner_args': {'name': 'div', 'attrs': {'class': 'inner--K9Svv'}},
                  'flow_topic_args': {'name':'a', 'attrs': {'class': 'item--ALUvj'}},
                  'flow_title_args': {'name': 'h4','attrs': {'class': 'heading--lf0qy'}},
                  'flows_cards_num' : 4, 'flows_units_per_card': 2
                  }
get_flow_news_args = {'article_card_args': {'name': 'div', 'attrs': {'class': 'item--LA1zO'}},
                      'article_link_args': {'name': 'a', 'attrs': {'class': 'link--aKZVS'}},
                      'article_author_args': {'name': 'div', 'attrs': {'class': 'name--ur745'}},
                      'article_date_args': {'name': 'time', 'attrs': {'class':'date--ZZJXU'}},
                      'article_views_args': {'name': 'span', 'attrs': {'class': 'counter--sXVCe'}},
                      'article_title_args': {'name': 'h3', 'attrs': {'class': 'title--Oe3sZ'}},
                      'article_likes_args': {'name': 'span', 'attrs': {'class': 'counter--fwxAj'}},
                      'article_comments_count_args': {'name': 'span', 'attrs': {'class': 'content--WdSlu'}},
                      'article_saves_count_args': {'name': 'button', 'attrs': {'class': 'favorites--y85P0'}},
                      'topic_args': {'name': 'h1', 'attrs': {'class': 'heading--lf0qy'}},
                      'news_per_page': 3, 'nums_pages': 2
                      }

flows_page_link = "https://journal.tinkoff.ru/flows/"


html = get_html(flows_page_link).content
flow_df = get_flows(html, get_flows_args)
flows_cards_df = parse_flows(flow_df['flow_link'].values, get_flow_news_args)
articles_content_df = get_articles_content(flows_cards_df['link'].values)
merged_df = flows_cards_df.merge(articles_content_df, on='link', how='left')
final_df = flow_df.merge(merged_df, on='flow_link', how='left')
final_df.to_csv(FILE)