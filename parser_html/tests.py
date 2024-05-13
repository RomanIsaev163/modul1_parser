import unittest
from utility import *
from parser_funcs import *

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

tink_host = 'https://journal.tinkoff.ru/flows/'
null_host = None
some_host = 'https://ya.ru'
broken_host = 'htps://ya.ru'
numeric_host = 5051


class TestParser(unittest.TestCase):
    def setUp(self):
        self.tink_host = tink_host
        self.null_host = null_host
        self.some_host = some_host
        self.broken_host = broken_host
        self.numeric_host = numeric_host

        self.tink_html = get_html(self.tink_host).content
        self.null_html = None
        self.empty_html = ''
        self.some_html = get_html(self.some_host).content

        self.tink_flows = get_flows(self.tink_html, get_flows_args)
        self.null_flows = None
        self.empty_flows = []
        self.random_flws = ['random', 'random']

    # get_html test cases 

    def test1_get_html(self):
        self.assertRaises(Exception, get_html(self.tink_host))

    def test2_get_html(self):
        self.assertRaises(Exception, get_html(self.some_host))

    def test3_get_html(self):
        self.assertRaises(Exception, get_html(self.null_host))

    def test4_get_html(self):
        self.assertRaises(Exception, get_html(self.broken_host))

    def test5_get_html(self):
        self.assertRaises(Exception, get_html(self.numeric_host))

    # get_flows test cases

    def test6_get_flows(self):
        self.assertRaises(Exception, get_flows(self.tink_html, get_flows_args))

    def test7_get_flows(self):
        self.assertRaises(Exception, get_flows(self.null_html, get_flows_args))

    def test8_get_flows(self):
        self.assertRaises(Exception, get_flows(self.empty_html, get_flows_args))

    def test9_get_flows(self):
        self.assertRaises(Exception, get_flows(self.some_html, get_flows_args))

    #  get_flows test cases

    def test10_parse_flow(self):
        self.assertRaises(Exception, parse_flows(self.tink_flows['flow_link'].values, get_flow_news_args))

    def test11_parse_flow(self):
        self.assertRaises(Exception, parse_flows(self.empty_flows, get_flow_news_args))

    def test12_parse_flow(self):
        self.assertRaises(Exception, parse_flows(self.null_flows, get_flow_news_args))

    def test13_parse_flow(self):
        self.assertRaises(Exception, parse_flows(self.random_flws, get_flow_news_args))


if __name__ == '__main__':
    unittest.main()
