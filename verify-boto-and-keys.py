import boto
import urllib2

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
awsKey = response.read().split(':')

accessId = awsKey[0]
accessKey = awsKey[1]

print(accessId)
print(accessKey)
print(boto.__version__)
