some utils I use for my personal scrapy projects. It's very opinionated, probably uses a lot of low quality shortcuts etc. so no promises if you use this.

Some features:
- helps with initial good default settings
- sets up Scrachy with DB backend for caching
- sets up a connection to a postgres DB from DATABASE_URL
- assumes all is running on dokku
- has some reporting to newrelic