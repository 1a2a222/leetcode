

import requests,json,re
from lxml import etree

class KrSpyder:
    def __init__(self):
        pass
    def run(self):
        #1.找到请求的url
        #2.发送请求，获取数据，获取下一页的数据
        #3.保存数据
        #4.继续请求