# simple_aws_crawler_framework

## Version info

- Python 3.6.9
- Scrapy 2.0.1
- Selenium 3.141.0
- Serverless 1.67.3

## Set env file

Create env directory in root path, and can add lambda environment variables in prod.yml 

```shell
/env
└── prod.yml
```

**e.g.**
```
# must add
CURRENT_ENV: prod

# option
ID: xxxxxxx
PASSWORD: xxxxxxx
```

## Deploy via serverless framework

`lxml` package needs to install on amazon linux, so should deploy on **EC2** or **Cloud9**.

```
sls deploy -v --aws-profile { aws_profile }
```

## Remove via serverless framework

```
sls remove -v --aws-profile { aws_profile }
```

## Local run

### default run

```
python launcher.py
```
The result of crawling will be recorded under the `/feed` directory

### other spider run

you can indicate specific spider file via json format.

```
python launcher.py {\"spider_name\":\"selenium_spider\"}
```

## Example

| spider_name | spider_explanation |
|---|---|
| default_spider | Fetch url and title from scrapy official web site |
| crawling_pagination_spider | Fetch my blog post title and link |
| selenium_screenshot_to_slack_spider | Access to google top page and save a screenshot. after that send it to slack channel|
| selenium_auth_spider | now preparing |

