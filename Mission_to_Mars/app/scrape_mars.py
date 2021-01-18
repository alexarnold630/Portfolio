#Jupyter Notebook Converstion to Python Script

#Imports
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
import time

class ScrapeMars():
    def __init__(self):
        pass

    def init_browser(self):
        # @NOTE: Replace the path with your actual path to the chromedriver
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)
        return browser

    def scrape_info(self):
        scraped_data = {}
        browser = self.init_browser()

        ########################################

        #NAASA Mars News Site
        news_url = "https://mars.nasa.gov/news/"
        browser.visit(news_url)
        time.sleep(1)

        soup = BeautifulSoup(browser.html)

        slide = soup.find("li", {"class": "slide"})
        news_title = slide.find("div", {"class": "content_title"}).text.strip()
        news_p = slide.find("div", {"class": "article_teaser_body"}).text.strip()

        ########################################

        #JPL Mars Space Images - Featured Image

        base = "https:www.jpl.nasa.gov"
        url = f"{base}/spaceimages/?search=&category=Mars"
        browser.visit(url)
        time.sleep(1)

        full_image_button = browser.find_by_id("full_image")
        full_image_button.click()
        time.sleep(1)

        more_info_button = browser.links.find_by_partial_text("more info")
        more_info_button.click()
        time.sleep(1)

        soup = BeautifulSoup(browser.html)
        image_url = soup.find("img", {"class": "main_image"})

        featured_image_url  = base + image_url["src"]

        ########################################

        #Mars Facts

        facts_url = "https://space-facts.com/mars/"
        browser.visit(facts_url)
        time.sleep(1)

        fact_df = pd.read_html(browser.html)
        facts_df = fact_df[0]
        facts_df.columns=["Description", "Mars"]
        mars_facts = facts_df.to_html(index=False)

        ########################################

        #Mars Hemispheres

        base_url = "https://astrogeology.usgs.gov"
        hemispheres_url = f"{base_url}/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(hemispheres_url)

        soup = BeautifulSoup(browser.html)

        links = soup.find("div", {"class": "results"}).findAll("a", {"class": "itemLink"})

        #Filtering out non image links
        image_links = []

        for link in links:
            image = link.find("img")
            if (image):
                image_links.append(base_url + link["href"])
                
        hemisphere_data = []
        for image_link in image_links:
            browser.visit(image_link)
            time.sleep(1)
            
            soup = BeautifulSoup(browser.html)
            image_url = soup.find("ul").find("li").find("a")["href"]
            hemisphere_title = soup.find("h2", {'class', "title"}).text.split(" Enhanced")[0]
            
            hemisphere_data.append({"title": hemisphere_title, "img_url": image_url})
            
        browser.quit()

        #Append Data
        scraped_data["news_title"] = news_title
        scraped_data["news_p"] = news_p
        scraped_data["featured_image_url"] = featured_image_url
        scraped_data["mars_facts"] = mars_facts
        scraped_data["hemispheres"] = hemisphere_data
        scraped_data["last_updated"] = datetime.datetime.now()
    
        return scraped_data
