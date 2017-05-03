# ec-auto
Automate using erlangcentral.org REST API 
Example URL: http://erlangcentral.org/wp-json/wp/v2/posts?categories=20

## Usage

```
$ python3 rest.py
{
    "job_company": "id3as",
    "job_end_date": "2017-06-30",
    "job_location": "Remote (GMT / CET)",
    "job_publish_date": "2017-03-31",
    "job_title": "Software Craftsman",
    "job_url": "https://erlangcentral.org/jobs/software-craftsman-id3as/"
}
{
    "job_company": "Discord",
    "job_end_date": "2017-04-30",
    "job_location": "San Francisco, CA",
    "job_publish_date": "2017-03-17",
    "job_title": "Software Engineer \u2013 Growth",
    "job_url": "https://erlangcentral.org/jobs/software-engineer-growth-discord/"
}
...
```
