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

```
python launcher.py
```

The result of crawling will be recorded under the `/feed` directory


