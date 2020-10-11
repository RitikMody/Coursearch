import json
import requests
import scrapy
from bs4 import BeautifulSoup

BASE_URL = "https://www.udacity.com/courses/all"

class UdacitySpider(scrapy.Spider):
    name = "udacity_spider"

    def __init__(self, *args, **kwargs):
	    super(UdacitySpider, self).__init__(*args, **kwargs)
	    self.search_term = kwargs.get('category')
	    self.start_urls = [BASE_URL]

    def parse(self, response):
        page = BeautifulSoup(response.body, 'lxml')
        courses = page.findAll("div", {"class": "catalog-component__card"})
        for course in courses:
            link_to_course = "https://www.udacity.com" + course.find('a', {'class': 'card__top'})["href"]

            skills = course.find("p", {"class": "text-content__text"})
            course_name = course.find("h2", {"class": "card__title__nd-name"}).text
            if self.search_term.lower() in course_name.lower() or skills and self.search_term.lower() in skills.text.lower():
                course_id = link_to_course.split("--")[-1]

                sections = list(course.find('div' , {'class': 'card__text-content'}).children)
                if len(sections) == 2:
                    partner_name = sections[1].find('p').text
                else:
                    partner_name = None

                image_link = "https://d20vrrgs8k4bvw.cloudfront.net/images/open-graph/udacity.png"

                difficulty_level = course.find('div', {'class': 'difficulty'}).find('small').text

                ratings_page = requests.get(f"https://ratings-api.udacity.com/api/v1/reviews?node={course_id}")
                rating_count = 0
                stats = json.loads(ratings_page.content)["stats"]
                avg_ratings = 0
                for stat in stats:
                    rating_count += stat["count"]
                    avg_ratings += stat["count"] * stat["rating"]
                if rating_count > 0:
                    avg_ratings = avg_ratings / rating_count
                rating_out_of_five = round(avg_ratings, 1)
                yield {
                    'course_name': course_name,
                    'partner_name': partner_name,
                    'image_link': image_link,
                    'rating_out_of_five': rating_out_of_five,
                    'rating_count': rating_count,
                    'difficulty_level': difficulty_level,
                    'link_to_course': link_to_course,
                    'offered_by': 'Udacity'
			    }
