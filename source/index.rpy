import ctypes
import json
import os
import boto3
import logging

# use python logging module to log to CloudWatch
# http://docs.aws.amazon.com/lambda/latest/dg/python-logging.html

logging.getLogger().setLevel(logging.DEBUG)

s3 = boto3.client('s3')

################### load R
# must load all shared libraries and set the
# R environment variables before you can import rpy2
# load R shared libraries from lib dir

for file in os.listdir('lib'):
    if os.path.isfile(os.path.join('lib', file)):
        ctypes.cdll.LoadLibrary(os.path.join('lib', file))

# set R environment variables
os.environ["R_HOME"] = os.getcwd()
os.environ["R_LIBS"] = os.path.join(os.getcwd(), 'site-library')

import rpy2
from rpy2 import robjects
from rpy2.robjects import r

################## end of loading R

def lambda_handler(event, context):
    try:
        total_value = event['total_value']

        # calling the get_prep_time function which predict the preparation time from the total_value in input
        prep_time = get_prep_time(total_value)

        res = {}
        res['prep_time'] = prep_time
        return res

    except Exception as e:
        logging.error('Payload: {0}'.format(event))
        logging.error('Error: {0}'.format(e.message))

        # generate a JSON error response that API Gateway will parse and associate with a HTTP Status Code

        error = {}
        error['errorType'] = type(e).__name__
        error['httpStatus'] = 500
        error['request_id'] = context.aws_request_id
        error['message'] = e.message.replace('\n', ' ') # convert multi-line message into single line
        raise Exception(json.dumps(error))

def get_prep_time(total_value):
    download_model_from_s3()
    r.assign('total_value', total_value)

    r('model <- readRDS("model.rds")')
    r('df <- data.frame(total_value=as.numeric(total_value)')
    r('prediction <- predict(model, newdata = df)')

    r_pred = robjects.r('prediction')

    # R return an array of one element. Return it
    return r_pred[0]


    def download_model_from_s3():
    # caching strategies used to avoid the download of the model.rds file every time from S3
    if os.path.isfile(RDS_FILE):
        logging.debug('file already downloaded')
        return
    else:
        bucket = '*** BUCKET NAME ***'
        key = 'model.rds'
    
        logging.debug('attempting to download file')
        try:
            s3.download_file(bucket,key,'model.rds')
        except Exception as e:
            logging.error('Error downloading file {} from bucket {}.'.format(key, bucket))
            logging.error(e)
            raise e