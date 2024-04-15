from aws_requests_auth.aws_auth import AWSRequestsAuth
from elasticsearch import Elasticsearch, RequestsHttpConnection
import os
from dotenv import load_dotenv
load_dotenv()
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
es_host = 'search-service-foobar.us-east-1.es.amazonaws.com'
auth = AWSRequestsAuth(aws_access_key=ACCESS_KEY,
                       aws_secret_access_key=SECRET_KEY,
                       aws_host='s3.tebi.io',
                       aws_region='us-east-1',
                       aws_service='s3')

# use the requests connection_class and pass in our custom auth class
es_client = Elasticsearch(host="s3.tebi.io",
                          port=80,
                          connection_class=RequestsHttpConnection,
                          http_auth=auth)
print(es_client)