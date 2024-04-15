import requests
from requests_auth_aws_sigv4 import AWSSigV4
import os
from dotenv import load_dotenv
load_dotenv()
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
aws_auth = AWSSigV4(service='s3',
                    region='us-east-1',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)
print(aws_auth)
#
# with open('video.mp4','rb') as f:
#     data = f.read()
#
# r = requests.request('PUT', 'https://progenz.s3.tebi.io/202512312.mp4',
#     auth=aws_auth,data=data)


# with open('video.mp4','wb') as f:
#     f.write(r.content)

