import boto3
import datetime
from botocore.client import Config
from requests import Request, Session

# Create S3 client object
s3 = boto3.client('s3', config=Config(signature_version='s3v4', region_name='us-east-1'))

# Define bucket and key name
YOUR_BUCKET = 'test'
KEY_NAME = 'test.txt'
#YOUR_KMS_KEY_ID = 'blah'
#PATH_TO_LOCAL_FILE = '/test.txt'

# Set object expiry time to be 604800 seconds after current time. Format must be in compliance with RFC 1123. (e.g. Thu, 01 Dec 1994 16:00:00 GMT)
expires = (datetime.datetime.now() + datetime.timedelta(0,604800)).strftime("%a, %d %b %Y %H:%M:%S GMT")

# Define ClientMethod paramters for pre-signed URL
params = {
    'Bucket': YOUR_BUCKET,
    'Key': KEY_NAME,
#    'Expires': expires,
#    'ServerSideEncryption': 'AES256',
#    'SSEKMSKeyId': YOUR_KMS_KEY_ID,
#    'ACL': 'private'
} 
      
# Generate the pre-signed URL
url = s3.generate_presigned_url(
    ClientMethod='put_object',
    Params=params
) 
         
# DEBUG: Print the presigned URL
print ('\ \ \ \ This is the presigned URL: ' + str(url) + '\ \ \ ')
