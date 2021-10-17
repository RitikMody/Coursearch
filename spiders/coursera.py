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

def scan(s):
	if s:
		return int(s.replace(',', '').replace('(', '').replace(')', ''))

def decimals(n):
	if n:
		return float(n)

def getCourses(driver, search_keyword):

	mylist = []
	
	for page in range(1, 4):
		driver.get(f"https://www.coursera.org/search?query={search_keyword}%p={page}")
		soup = BeautifulSoup(driver.page_source, "lxml")
		for course in soup.select("li.ais-InfiniteHits-item"):
			mydict = {}
			NAME_SELECTOR = ".card-title"
			PARTNER_SELECTOR = 'span.partner-name'
			IMAGE_SELECTOR = 'div.card-content div.cds-grid-item img'
			RATING_SELECTOR = ".ratings-text"
			NUM_RATINGS_SELECTOR = "span.ratings-count span"	
			DIFFICULTY_SELECTOR = ".difficulty"
			LINK_SELECTOR = "div a"
			mydict["course_name"] = course.select_one(NAME_SELECTOR).text
			mydict["partner_name"] = course.select_one(PARTNER_SELECTOR).text
			mydict["image_link"] = course.select_one(IMAGE_SELECTOR)['src']
			mydict["rating_out_of_five"] = decimals(course.select_one(RATING_SELECTOR).text)
			mydict["rating_count"] = scan(course.select_one(NUM_RATINGS_SELECTOR).text)
			mydict["difficulty_level"] = course.select_one(DIFFICULTY_SELECTOR).text
			mydict["link_to_course"] = 'https://www.coursera.org' + course.select_one(LINK_SELECTOR)['href']
			mydict["offered_by"] = "Coursera"
			mylist.append(mydict)
	return mylist

def func(search_keyword):
	driver = configure_driver()
	list = getCourses(driver,search_keyword)
	driver.close()
	return list
