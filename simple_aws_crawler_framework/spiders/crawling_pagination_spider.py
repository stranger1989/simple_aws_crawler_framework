import scrapy
from simple_aws_crawler_framework.items import Post

from scrapy.spiders import CrawlSpider


class CrawlingPaginationSpiderSpider(CrawlSpider):
    name = "crawling_pagination_spider"
    allowed_domains = ['blank-oldstranger.com']
    start_urls = ['https://blank-oldstranger.com']

    def parse(self, response):
        for post in response.css('.entry-card-wrap'):
            # create post object
            yield Post(
                url=post.css('a::attr(href)').extract_first().strip(),
                title=post.css('div.entry-card-content h2::text').extract_first().strip(),
            )

        # trace pagination
        older_post_link = response.css('.pagination a.next::attr(href)').extract_first()
        if older_post_link is None:
            # if the next is none, it's finished.
            return

        older_post_link = response.urljoin(older_post_link)
        # implement next page
        yield scrapy.Request(older_post_link, callback=self.parse)
