
from bs4 import BeautifulSoup 
import requests
import ipdb

class Scraper:

    def __init__(self):
      self.courses = []

    def get_page():
        doc =  BeautifulSoup(requests.get("http://learn-co-curriculum.github.io/site-for-scraping/courses").text, 'html.parser')
        ipdb.set_trace()

Scraper.get_page()