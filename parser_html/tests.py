import unittest
from utility import *

tink_host = 'https://journal.tinkoff.ru/'
null_host = None
some_host = 'https://ya.ru'
broken_host = 'htps://ya.ru'
numeric_host =  5051

class TestParser(unittest.TestCase):
    def setUp(self):

        self.tink_host = tink_host
        self.null_host = null_host
        self.null_host = some_host
        self.broken_host = broken_host
        self.numeric_host = numeric_host
        
    # get_html test casec function 
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
            
unittest.main()