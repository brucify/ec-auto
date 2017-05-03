import json
from urllib.request import urlopen

url = 'http://erlangcentral.org/wp-json/wp/v2/posts?categories=20'
json_result = json.load(urlopen(url))
one_post = json_result[2]

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

    print (json.dumps(data, indent=4, sort_keys=True))
