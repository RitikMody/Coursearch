import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import pandas as pd
import json

def scan(s):
	if s:
		return int(s[s.index(">") + 1: s.index("<", 1)].replace(',', ''))

def decimals(n):
	if n:
		return float(n)

df1=pd.DataFrame()

class CourseraSpider(scrapy.Spider):
	name = 'coursera_spider'
	def __init__(self, *args, **kwargs):
		super(CourseraSpider, self).__init__(*args, **kwargs)
		searchterm = kwargs.get('category')
		searchterm = ('%20').join(searchterm.lower().split())
		self.start_urls = [f'https://www.coursera.org/search?query={searchterm}&page='
				  + str(i) + '&index=prod_all_products_term_optimization' for i in [1, 2, 3]]

	params = {'course_name':[],
            'link_to_course':[],
            'partner_name':[],
            'rating_out_of_five':[],
            'rating_count':[],
            'image_link':[],
            'difficulty_level':[],
            'offered_by':[]}

	df = pd.DataFrame(params)

	def parse(self, response):
		COURSE_SELECTOR = './/li[@class="ais-InfiniteHits-item"]'
		for course in response.xpath(COURSE_SELECTOR):

			NAME_SELECTOR = '.headline-1-text::text'
			PARTNER_SELECTOR = '.partner-name::text'
			IMAGE_SELECTOR = './/div[@class="vertical-box"]//div[@class="image-wrapper"]//img/@src'
			RATING_SELECTOR = '.ratings-text::text'
			NUM_RATINGS_SELECTOR = './/span[@class="ratings-count"]//span'
			DIFFICULTY_SELECTOR = '.difficulty::text'
			LINK_SELECTOR = './div/a/@href'
			self.df = self.df.append({'course_name': course.css(NAME_SELECTOR).extract_first(),
					'partner_name': course.css(PARTNER_SELECTOR).extract_first(),
					'image_link': course.xpath(IMAGE_SELECTOR).extract_first(),
					'rating_out_of_five': decimals(course.css(RATING_SELECTOR).extract_first()),
					'rating_count': scan(course.xpath(NUM_RATINGS_SELECTOR).extract_first()),
					'difficulty_level': course.css(DIFFICULTY_SELECTOR).extract_first(),
					'link_to_course': 'https://www.coursera.org' + course.xpath(LINK_SELECTOR).extract_first(),
					'offered_by': 'Coursera'},
                            ignore_index = True
                            )
			global df1 
			df1 = self.df
			# yield {
			# 	'course_name': course.css(NAME_SELECTOR).extract_first(),
			# 	'partner_name': course.css(PARTNER_SELECTOR).extract_first(),
			# 	'image_link': course.xpath(IMAGE_SELECTOR).extract_first(),
			# 	'rating_out_of_five': decimals(course.css(RATING_SELECTOR).extract_first()),
			# 	'rating_count': scan(course.xpath(NUM_RATINGS_SELECTOR).extract_first()),
			# 	'difficulty_level': course.css(DIFFICULTY_SELECTOR).extract_first(),
			# 	'link_to_course': 'https://www.coursera.org' + course.xpath(LINK_SELECTOR).extract_first(),
			# 	'offered_by': 'Coursera'
			# }