import scrapy

# Simply gather the list of deck archetypes visible from start_urls and copy it in a *txt file
class ArchetypeSpider(scrapy.Spider):
    
    name = 'archetypes'
    allowed_domains = ['www.mtgtop8.com']
    start_urls = ['https://www.mtgtop8.com/format?f=LE']


    def parse(self, response):
        href_list =[]
        for anchor in response.css('td > table.Stable a'): # CSS selector for archetypes
            href_list.append(anchor.css("a::attr(href)").get())
            
        archetypes_list = [href for href in href_list if 'archetype?a=' in href]
        with open('archetypeslist.txt','w') as f:
            lines = '\n'.join(['http://mtgtop8.com/'+a for a in archetypes_list])
            f.write(lines)
