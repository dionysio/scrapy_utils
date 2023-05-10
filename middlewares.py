from scrapy import signals
import newrelic.agent


class SaveJobInDatabase:
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def spider_closed(self, spider, reason):
        application = newrelic.agent.application()

        stats = spider.crawler.stats.get_stats()
        stats.update({
            'job_id': spider.job_id,
            'run_id': spider.run_id,
            'spider': spider.name
        })

        newrelic.agent.record_custom_event("ScrapyEvent", stats, application)
