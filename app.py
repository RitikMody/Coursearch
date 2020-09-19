import crochet
crochet.setup()

from flask import Flask , render_template, jsonify, request, redirect, url_for ,make_response,send_from_directory
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
import time
from spiders import *
import pandas as pd

app = Flask(__name__)

output_data = []
crawl_runner = CrawlerRunner()

def scrape(searchTerm):
    scrape_with_crochet(searchTerm=searchTerm ,spider = udemy.UdemySpider) 
    scrape_with_crochet(searchTerm=searchTerm ,spider = coursera.CourseraSpider) 
    time.sleep(5)
    output_data.extend(pluralsight.getCourses(searchTerm))
    # output_data.extend(udacity.getCourses(searchTerm))
    df = pd.DataFrame()
    for i in output_data:
        df = df.append(i,ignore_index= True)
    output_data.clear()
    return df

@app.route('/')
def hello_world():
    df = scrape("deep learning")
    return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/docs')
def docs():
    return render_template('docs.html')

@app.route('/api',methods = ['GET'])
def api():
    args = request.args
    if(len(args)==2):
        if(args["site"]=="udemy"):
            scrape_with_crochet(searchTerm=args["searchTerm"] ,spider= udemy.UdemySpider)
            time.sleep(2)
        elif(args["site"]=="coursera"):
            scrape_with_crochet(searchTerm=args["searchTerm"] ,spider= coursera.CourseraSpider) 
            time.sleep(2)
        elif(args["site"]=="pluralsight"):
            output_data.extend(pluralsight.getCourses(args["searchTerm"]))

    else:
        scrape_with_crochet(searchTerm=args["searchTerm"] ,spider= udemy.UdemySpider) 
        scrape_with_crochet(searchTerm=args["searchTerm"] ,spider= coursera.CourseraSpider) 
        time.sleep(5)
        output_data.extend(pluralsight.getCourses(args["searchTerm"]))
    res = jsonify(output_data)
    output_data.clear()
    return res



@crochet.run_in_reactor
def scrape_with_crochet(searchTerm,spider):
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    
    eventual = crawl_runner.crawl(spider, category = searchTerm)
    return eventual

def _crawler_result(item, response, spider):
    output_data.append(dict(item))

if __name__ == '__main__':
   app.run(debug=False)