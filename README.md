# Deploy the spider to Scrapy Cloud
 shub deploy

 scrapy genspider mydomain mydomain.com

 scrapy genspider apple apple.com
 
pip freeze > requirements.txt

pip install -r requirements.txt
 
scrapy crawl itunes
 
scrapyd-deploy local -p katph 
curl http://localhost:6800/schedule.json -d project=katph -d spider=itunes