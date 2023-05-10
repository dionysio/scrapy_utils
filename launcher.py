import logging
from functools import wraps
import json
import sys

from scrapy.spiderloader import SpiderLoader
from scrapy.crawler import CrawlerProcess

from .log import setup_log
from .newrelic_cron import newrelic_cron


def scrapy_launcher(func):
    @wraps(func)
    def _wrapped(event, context=None):
        job_id, project_settings = setup_log()
        process = CrawlerProcess({**project_settings, **event.get('settings', {})}, install_root_handler=False)

        return func(process=process, event=event, context=context, job_id=job_id, project_settings=project_settings)
    return _wrapped


def get_spiders(project_settings, requested_spiders=None):
    if requested_spiders is None:
        requested_spiders = []
    loader = SpiderLoader(project_settings)

    logging.info("implemented spiders: {}".format(', '.join(loader._spiders.keys())))
    for name, spider_cls in loader._spiders.items():
        if requested_spiders and name not in requested_spiders:
            logging.info(f"skipping {name} spider")
            continue
        yield name, spider_cls


@scrapy_launcher
def run_spiders(process, project_settings, job_id, event, **kwargs):
    state = event.get('state', {})
    for name, spider_cls in get_spiders(project_settings, event.get('spiders')):
        logging.info(f"starting {name} spider")
        process.crawl(spider_cls, state=state, job_id=job_id)
    return process.start()


def main():
    try:
        cmd_args = json.loads(sys.argv[1])
    except (IndexError, json.decoder.JSONDecodeError):
        cmd_args = {}
    return newrelic_cron(run_spiders)(cmd_args)


if __name__ == "__main__":
    main()
