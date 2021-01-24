import scrapy
import selenium
from selenium import webdriver
import re

regex = r"event(.*)d(.*)LE"


class DeckLinksSpiderSelenium(scrapy.Spider):
    
    acum = ''
    name = 'links_selenium'
    allowed_domains = ['www.mtgtop8.com']
    start_urls = start_urls = ['https://www.mtgtop8.com/format?f=LE']

    geckodriver_path = 'blablabla' #Path to your geckodriver exe
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=geckodriver_path)

    def parse(self, response):
        
        with open('archetypeslist.txt','r') as links:
            urls = links.read().split('\n')[:-1]
            href_list =[]

        for url in urls:
            self.driver.get(url)
            list_href = self.driver.find_elements_by_class_name('Stable')[1].find_elements_by_css_selector('td a')
            for href in list_href:
                href_list.append(href.get_attribute('href')) 

            nb_page = len(self.driver.find_elements_by_class_name('Nav_norm'))
            
            try:
                while self.driver.find_elements_by_class_name('Nav_PN')[-1].text == 'Next':
                    next_page = self.driver.find_elements_by_class_name('Nav_PN')
                    next_page[-1].click()
                    list_href = self.driver.find_elements_by_class_name('Stable')[1].find_elements_by_css_selector('td a')
                    for href in list_href:
                        href_list.append(href.get_attribute('href'))
            except:
                print('There is only one page!')
                list_href = self.driver.find_elements_by_class_name('Stable')[1].find_elements_by_css_selector('td a')
                for href in list_href:
                    href_list.append(href.get_attribute('href'))

        cont = '\n'.join([hr for hr in href_list])
        self.acum += cont

        matches = re.finditer(regex, self.acum, re.MULTILINE)
        match_list = []
        
        for matchNum, match in enumerate(matches, start=1):
            match_list.append(match.group())

        #Remove duplicate... just in case
        match_list = list(set(match_list))

        with open('decklists.txt','w') as f:
            f.write('\n'.join(['http://mtgtop8.com/'+match for match in match_list]))

        self.driver.close()

