# Scrapy settings for my_scrapy_project project

BOT_NAME = "my_scrapy_project"

SPIDER_MODULES = ["my_scrapy_project.spiders"]
NEWSPIDER_MODULE = "my_scrapy_project.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 0.5  # Adjust to balance speed and server load
CONCURRENT_REQUESTS_PER_DOMAIN = 8  # Concurrent requests for the same domain
CONCURRENT_REQUESTS_PER_IP = 8  # Concurrent requests per IP

# Retry failed requests
RETRY_ENABLED = True
RETRY_TIMES = 5  # Number of retries
RETRY_HTTP_CODES = [500, 502, 503, 504, 403, 408]

# Enable or disable Telnet Console
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 100,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 200,
}

# Enable item pipelines for media
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
    'scrapy.pipelines.files.FilesPipeline': 2,
    'my_scrapy_project.pipelines.S3Pipeline': 300,
}

# Enable Scrapy Proxy Pool
PROXY_POOL_ENABLED = True

# Set Media URL paths
IMAGES_STORE = 'images'
FILES_STORE = 'files'

# HTTP Cache settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [500, 502, 503, 504, 403, 404]
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# TLS settings for Scrapy
DOWNLOADER_CLIENT_TLS_METHOD = 'TLS'
DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING = True
DOWNLOADER_CLIENT_TLS_CIPHERS = 'ECDHE+AESGCM:ECDHE+CHACHA20:ECDHE+SHA256:!SSLv3:!TLSv1:!TLSv1.1'

# Splash settings
SPLASH_URL = 'https://splash-service-rfid.onrender.com'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

# Limit the depth of scraping
DEPTH_LIMIT = 5  # Adjust based on how deep you want to scrape

# Prioritize deeper requests
DEPTH_PRIORITY = 1

# Set download timeout to avoid hanging
DOWNLOAD_TIMEOUT = 15

# Auto-throttling settings
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1  # Initial delay for requests
AUTOTHROTTLE_MAX_DELAY = 10  # Max delay in case of high latencies
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # Number of requests in parallel
AUTOTHROTTLE_DEBUG = False

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
FEED_EXPORT_ENCODING = "utf-8"
