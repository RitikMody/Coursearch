import json
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

def configure_driver():
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	# chrome_options = Options()
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	# driver = webdriver.Chrome(executable_path="chromedriver.exe", options = chrome_options)
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options = chrome_options)
	return driver

def formatreviews(x):
	if x:
		n = ''.join([i for i in str(x) if i.isdigit()])
	else:
		n = 0
	return n

def count_stars(s):
	s = str(s)
	ones = s.count('<i class="fa fa-star"></i>')
	halves = s.count('<i class="fa fa-star-half-o"></i>')
	total = ones + halves * 0.5
	return total
    

def getCourses(driver, search_keyword):

	driver.get(f"https://www.pluralsight.com/search?q={search_keyword}&categories=course")
	try:
		WebDriverWait(driver, 5).until(lambda s: s.find_element_by_id("search-results-category-target").is_displayed())
	except TimeoutException:
		print("TimeoutException: Element not found")
		return None
    
	soup = BeautifulSoup(driver.page_source, "lxml")
	mylist = []
	
	for course_page in soup.select("div.search-results-page"):	
		for course in course_page.select("div.search-result"):
			mydict = {}
			TITLE_SELECTOR = "div.search-result__info div.search-result__title a"
			AUTHOR_SELECTOR = "div.search-result__details div.search-result__author"
			LEVEL_SELECTOR = "div.search-result__details div.search-result__level"
			RATING_SELECTOR = "div.search-result__details div.search-result__rating"
			REVIEWS_SELECTOR = "div.search-result__details div.search-result__rating"
			IMAGE_SELECTOR = "div.search-result__icon img"
			LINK_SELECTOR = "div.search-result__info div.search-result__title a"
			if course.select_one(RATING_SELECTOR) and len(str(course.select_one(REVIEWS_SELECTOR)))!=0:
				try:
					mydict["course_name"] = course.select_one(TITLE_SELECTOR).text
					mydict["partner_name"] = (course.select_one(AUTHOR_SELECTOR).text).replace('by ', '')
					mydict["difficulty_level"] = course.select_one(LEVEL_SELECTOR).text
					mydict["rating_out_of_five"] = count_stars(course.select_one(RATING_SELECTOR))
					mydict["rating_count"] = int(formatreviews(course.select_one(REVIEWS_SELECTOR)))
					mydict["image_link"] = course.select_one(IMAGE_SELECTOR)['src']
					mydict["offered_by"] = "Pluralsight"
					mydict["link_to_course"] = course.select_one(LINK_SELECTOR)['href']
					mylist.append(mydict)
				except:
					pass
	return mylist

def func(search_keyword):
	driver = configure_driver()
	list = getCourses(driver,search_keyword)
	driver.close()
	return list
