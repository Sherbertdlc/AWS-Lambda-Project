import boto3
# Create S3 and SNS clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

# Define the Lambda handler function
def lambda_handler(event, context):

    # Get the bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Get the file object from S3
    info = s3.get_object(Bucket=bucket, Key=key)

    # Read the file content as a string
    contents = info['Body'].read()

    # Count the number of words in the file
    word_count = contents.split()

    # Create the message body
    message = "The word count in the "+key+" file is "+ str(len(word_count))+" words."

    # Define the SNS topic ARN
    sns_topic_arn = 'arn:aws:lambda:us-west-2:730335594069:function:AWSLambdaChallenge'

    # Publish the message to the SNS topic
    response = sns.publish(TopicArn=sns_topic_arn, Message=message, Subject='Word Count Result')
