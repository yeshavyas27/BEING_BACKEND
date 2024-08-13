# import scrapy
# from twisted.internet import reactor, defer
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from scrapy.utils.project import get_project_settings
# import re
#
# from global_utilities import exercises
#
# exercise_urls = []
# exercises_list = []
#
#
# class GetPostsURLSpider(scrapy.Spider):
#     name = "exercises_urls"
#     start_urls = [
#         "https://yogajala.com/yoga-poses/",
#     ]
#
#     def parse(self, response):
#
#         for post in response.css("li.wp-block-post"):
#             post_page_link = post.css('li.wp-block-post h4 a::attr("href")').get()
#             exercise_urls.append(post_page_link)
#
#
# class GetPostsDataSpider(scrapy.Spider):
#     name = "exercises_data"
#     start_urls = exercise_urls
#     def parse(self, response):
#         name = re.sub(r'\s*\(.*?\)', '', response.css("h1.entry-title::text").get())
#         image_url = response.css("div.entry-content figure.wp-block-image img::attr('data-lazy-src')").get()
#         p_tag = response.xpath('/html/body/div[1]/div/div[1]/main/article/div/div[1]/p[contains(text(), "Pose Type: ")]')
#         tags = p_tag.css('a::text').getall() if p_tag else []
#         tags = [tag.replace('\xa0', '') for tag in tags]
#         instructions = ""
#         ol_tag = response.css("div.entry-content ol")
#
#         if ol_tag:
#             ol_elements = response.css('div.entry-content ol')
#
#             for ol in ol_elements:
#                 # Select all <li> elements within the <ol>
#                 li_elements = ol.xpath('.//li')
#
#                 for li in li_elements:
#                     # Extract the text content of each <li> element
#                     li_text = li.xpath('normalize-space(string())').get()
#                     instructions += li_text
#         else:
#             divs = response.css('div.entry-content')
#             for div in divs:
#                 # Extract text directly from the <div> itself if it starts with a number followed by a period
#                 div_text = div.xpath('normalize-space(string())').get()
#                 if div_text and re.match(r'^\d+\.', div_text):
#                     print(div_text)
#
#                 # Extract text from descendant <p> elements if they start with a number followed by a period
#                 p_elements = div.css('p')
#                 for p in p_elements:
#                     p_text = p.xpath('normalize-space(string())').get()
#                     if p_text and re.match(r'^\d+\.', p_text):
#                         p_text = re.sub(r'\b\d+\.\s*', '', p_text)
#                         p_text = re.sub(r'\b\d+\s*', '', p_text)
#                         p_text = p_text.replace('\xa0', ' ')
#
#                         instructions += p_text
#         tags.append("Yoga")
#         exercises_list.append(
#             {
#                 "name": name,
#                 "image_url": image_url,
#                 "tags": tags,
#                 "instruction": instructions,
#             }
#         )
#
#
# def scrape_exercises():
#
#     settings = get_project_settings()
#     configure_logging(settings)
#     runner = CrawlerRunner(settings)
#
#     @defer.inlineCallbacks
#     def crawl():
#         yield runner.crawl(GetPostsURLSpider)
#         yield runner.crawl(GetPostsDataSpider)
#         reactor.stop()
#
#     crawl()
#     reactor.run()
#
# scrape_exercises()
# print(exercises_list)
# # for exercise in exercises_list:
# #     exercise["created_by"] = "scraper"
# #     exercises.insert_one(exercise)
#
#
#
#
#
#
#
#
#
#
