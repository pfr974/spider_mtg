import scrapy

class DeckSpider(scrapy.Spider):
    
    name = 'decklists_raw'
    allowed_domains = ['www.mtgtop8.com']
    start_urls = ['https://www.mtgtop8.com/format?f=LE']

    count = 0

    def start_requests(self):

        with open('decklists.txt','r') as links:
            urls = links.read().split('\n')[:-1]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        deck_list = response.css('td > table.Stable tr > td.G14').getall()# CSS selector
        cont = str(deck_list)
        self.count+=1
        with open('decks_raw/deck_'+str(self.count)+'.html','w') as f:
            f.write(cont)