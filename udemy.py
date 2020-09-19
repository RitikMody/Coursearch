import scrapy
from scrapy.crawler import CrawlerProcess
import json
import pandas as pd

# df1=pd.DataFrame()

class UdemySpider(scrapy.Spider):

    name = 'udemy_spider'
    def __init__(self, *args, **kwargs):
        super(UdemySpider, self).__init__(*args, **kwargs)
        searchterm = kwargs.get('category')
        searchterm = ('%20').join(searchterm.lower().split())
        self.start_urls = [f'https://www.udemy.com/api-2.0/search-courses/?p='+str(i)+'&q='+searchterm+'&skip_price=true' for i in (1, 2, 3)]
        self.headers={"accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.udemy.com/courses/search/?q="+searchterm,
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-udemy-cache-brand": "UAen_US",
    "x-udemy-cache-campaign-code": "UDEMYBASICS0720",
    "x-udemy-cache-device": "desktop",
    "x-udemy-cache-language": "en",
    "x-udemy-cache-logged-in": "0",
    "x-udemy-cache-marketplace-country": "UA",
    "x-udemy-cache-modern-browser": "1",
    "x-udemy-cache-price-country": "UA",
    "x-udemy-cache-release": "a50355e6f369173f712c",
    "x-udemy-cache-user": "",
    "x-udemy-cache-version": "1"
    }
    
    # params = {'course_name':[],
    #         'link_to_course':[],
    #         'partner_name':[],
    #         'rating_out_of_five':[],
    #         'rating_count':[],
    #         'image_link':[],
    #         'difficulty_level':[],
    #         'offered_by':[]}

    # df = pd.DataFrame(params)
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers )

    def parse(self, response):
        data = json.loads(response.text)
        for i in data['courses']:
            # self.df = self.df.append({'course_name':i['title'],
            #                 'link_to_course':"https://www.udemy.com"+i['url'],
            #                 'partner_name':i['visible_instructors'][0]['title'],
            #                 'rating_out_of_five':i['rating'],
            #                 'rating_count':i['num_reviews'],
            #                 'image_link':i['image_240x135'],
            #                 'difficulty_level':i['instructional_level'],
            #                 'offered_by':'Udemy'},
            #                 ignore_index = True
            #                 )
            
            yield{
                'course_name':i['title'],
                'link_to_course':"https://www.udemy.com"+i['url'],
                'partner_name':i['visible_instructors'][0]['title'],
                'rating_out_of_five':i['rating'],
                'rating_count':i['num_reviews'],
                'image_link':i['image_240x135'],
                'difficulty_level':i['instructional_level'],
                'offered_by':'Udemy'
            }
#         # global df1 
#         # df1 = self.df

# if __name__=="__main__":
#     process =CrawlerProcess()
#     process.crawl(UdemySpider)
#     process.start()

# def run(searchTerm):
#     process =CrawlerProcess()
#     process.crawl(UdemySpider, category = searchTerm)
#     process.start()
#     return df1