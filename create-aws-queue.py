import sys
import boto.sqs
import boto.sqs.queue
import urllib2
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

if (len(sys.argv) != 2):
    sys.exit('Usage: python create-aws-queue.py queue_name')
    
queueName = sys.argv[1]

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
awsKey = response.read().split(':')
access_key_id = awsKey[0]
secret_access_key = awsKey[1]

conn = boto.sqs.connect_to_region('eu-west-1', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

try:
    rs = conn.create_queue(queueName)
    print('queue ' + queueName + ' is now created')
except Exception, e:
    print(e)
