# -*- coding: utf-8 -*-

import os
import random
import re


def get_scrapy_settings(project_name=''):
    settings = dict((("BOT_NAME", os.getenv('DOKKU_APP_NAME') or project_name),

            ("USER_AGENT", random.choice((
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                                         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                                         "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
                                         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5351.0 Safari/537.36",
                                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15",
                                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0",
                                         "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
                                         "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
                                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0",
                                         "Mozilla/5.0 (Windows NT 10.0; rv:110.0) Gecko/20100101 Firefox/110.0",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50",
                                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
                                         "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57",
                                         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
                                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
                                         "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/109.0",
                                         "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
                                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.46"))),

            ("ROBOTSTXT_OBEY", False),

            ("CONCURRENT_REQUESTS", os.getenv('CONCURRENT_REQUESTS', 4)),
            ("REQUEST_FINGERPRINTER_IMPLEMENTATION", '2.7'),
            ("DOWNLOAD_DELAY", os.getenv('DOWNLOAD_DELAY', 1)),

            ("COOKIES_ENABLED", True),

            ("SPIDER_MIDDLEWARES", {'scrapy_utils.middlewares.SaveJobInDatabase': 300}),

            ("DOWNLOADER_MIDDLEWARES", {
                'scrachy.middleware.ignorecached.IgnoreCachedResponse': 50,
                'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 1000}),

            ("EXTENSIONS", {'scrapy_fieldstats.fieldstats.FieldStatsExtension': 10}),
            ("FIELDSTATS_ENABLED", True),
            ("FIELDSTATS_COUNTS_ONLY", True),

            ("HTTPCACHE_ENABLED", True),
            ("HTTPCACHE_EXPIRATION_SECS", 30000000),
            ("HTTPCACHE_STORAGE", 'scrachy.middleware.httpcache.AlchemyCacheStorage'),

            ("FEED_FORMAT", 'json'),
            ("LOG_LEVEL", os.getenv('LOG_LEVEL', 'DEBUG')),

            ("CLOSESPIDER_ITEMCOUNT", os.getenv('CLOSESPIDER_ITEMCOUNT', 0)),
            ("CLOSESPIDER_ERRORCOUNT", os.getenv('CLOSESPIDER_ERRORCOUNT', 10)),
            ("SCRACHY_CREDENTIALS_FILE", 'scrachy_credentials.txt'),
    ))

    settings.update(dict((
        ("SPIDER_MODULES", [f'{settings["BOT_NAME"]}.spiders']),
        ("NEWSPIDER_MODULE", f'{settings["BOT_NAME"]}.spiders'),
        ("DATABASE_URL", os.getenv('DATABASE_URL', f'postgresql://admin:admin@localhost:5432/{settings["BOT_NAME"]}')),
        ("SCRACHY_REGION_NAME", settings["BOT_NAME"]))))

    if settings['DATABASE_URL'].startswith("postgres://"):
        settings["DATABASE_URL"] = settings['DATABASE_URL'].replace("postgres://", "postgresql://", 1).replace('postgis_database', settings['BOT_NAME'], 1)

    settings.update(dict(zip(('SCRACHY_DIALECT', 'DB_USERNAME', 'DB_PASSWORD', 'SCRACHY_HOST', 'SCRACHY_PORT', 'SCRACHY_DATABASE'), re.findall('([^:]*)://([^:]*):([^@]*)@([^:]*):([^/]*)/([^:]*)', settings['DATABASE_URL'])[0])))

    with open('scrachy_credentials.txt', 'w') as credentials_file:
        credentials_file.write(f"username={settings['DB_USERNAME']}\npassword={settings['DB_PASSWORD']}")

    if os.getenv('DOKKU_APP_TYPE'):
        settings['ENV'] = 'PROD'
    else:
        settings['ENV'] = 'DEV'

    return settings
