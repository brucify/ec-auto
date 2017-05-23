import json
from urllib.request import urlopen
import time
from datetime import date


url = 'http://erlangcentral.org/wp-json/wp/v2/posts?categories=20&per_page=40'
json_result = json.load(urlopen(url))
one_post = json_result[2]
jobs = []

for one_post in json_result:

    job_title = one_post['title']['rendered']
    job_publish_date = one_post['date'][:10]
    job_url = one_post['link']

    if 'post_meta' in one_post:
        job_company = one_post['post_meta']['company']
        job_end_date = one_post['post_meta']['expiredate']
        job_location = one_post['post_meta']['location']
    else:
        job_company = ''
        job_end_date = ''
        job_location = ''

    data = {'job_title': job_title,
    'job_company': job_company,
    'job_publish_date': job_publish_date,
    'job_end_date': job_end_date,
    'job_url': job_url,
    'job_location': job_location}

    if date.today().isoformat() < job_end_date:
        # print (json.dumps(data, indent=4, sort_keys=True))
        print(data['job_title'].encode('ascii', 'ignore').decode('ascii'))
        print(data['job_company'] + " - " + data['job_location'])
        print(data['job_url'])
        print("\n")
        jobs.append(data)


print (len(jobs))
