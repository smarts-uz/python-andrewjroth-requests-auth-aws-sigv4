import requests
from aws_requests_auth.aws_auth import AWSRequestsAuth
import os
from dotenv import load_dotenv
load_dotenv()
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
# let's talk to our AWS Elasticsearch cluster
auth = AWSRequestsAuth(aws_access_key=ACCESS_KEY,
                       aws_secret_access_key=SECRET_KEY,
                       aws_host='s3.tebi.io',
                       aws_region='us-east-1',
                       aws_service='s3')

response = requests.get('https://s3.tebi.io',
                        auth=auth)
print(response.content)