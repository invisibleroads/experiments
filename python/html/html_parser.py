'''
python html_parser.py "<a href=""><img/></a><script async>"
'''
from html.parser import HTMLParser
from sys import argv


class TemplateFilter(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('handle_starttag', tag, attrs)

    def handle_startendtag(self, tag, attrs):
        print('handle_startendtag', tag, attrs)

    def handle_endtag(self, tag):
        print('handle_endtag', tag)

    def handle_data(self, data):
        print('handle_data', data)


f = TemplateFilter()
f.feed(argv[1])
