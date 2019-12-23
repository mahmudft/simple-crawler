# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['code.tutsplus.com/courses#']
    start_urls = ['http://code.tutsplus.com/courses#/']

    def parse(self, response):
        courses = response.xpath('//ol[@class="posts posts--full-width"]')

        for course in courses:
            author = course.xpath('.//div[@class="posts__post-publication-meta"]/img/@alt').extract_first()
            title = course.xpath('.//a[@class="posts__post-title "]/h1/text()').extract_first()
            description = course.xpath('.//div[@class="posts__post-teaser"]/text()').extract_first()
            release_date = course.xpath('.//time[@class="posts__post-publication-date"]/@title').extract_first()
            course_type=course.xpath('.//a[@class="posts__post-primary-category-link topic-cod"]/text()').extract_first()
            duration=course.xpath('.//span[@class="posts__post-extra-info"]/text()').extract_first()
            yield {
                'author': author,
                'title': title,
                'description': description,
                'release_date': release_date,
                'course_type': course_type,
                'duration': duration,
            }
            print(response)

