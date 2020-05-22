import scrapy


class GooglescholarItem(scrapy.Item):
    # fields that are extracted:
     name = scrapy.Field()
     email = scrapy.Field()
     tags = scrapy.Field()
     position = scrapy.Field()
     citation = scrapy.Field()
     citation_2014 = scrapy.Field()
     hindex = scrapy.Field()
     hindex_2014 = scrapy.Field()
     iindex = scrapy.Field()
     iindex_2014 = scrapy.Field()
     totaltitle = scrapy.Field()
     maxyear = scrapy.Field()
     minyear = scrapy.Field()
    
