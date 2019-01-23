# - * - encoding: utf-8 - * -
# Author: Gabriel Tagliani -- 2018-10-10
# Requirements:
# - Credentials aws(integrated in your terminal), boto, os, python2 or python3
# If you need: pip install boto, pip install os.

import boto, os

LOCAL_PATH = '../../../../../../../S3 DOWNLOAD/' #Directory on which files will be saved
bucket_name = 'dl-hsa-dev-data'                  #Name of the bucket that will be downloaded
conn = boto.connect_s3()                         # Connecting to S3
bucket = conn.get_bucket(bucket_name)            # Connecting to bucket

def downloadArq(bucket):
  arq = 0
  for l in bucket.list(prefix='fato_pd_peca'): #! Name the bucke where will be operated your download
    arq += 1
    keyString = str(l.key)
    d = LOCAL_PATH + keyString
    print('%s %s' %(arq,d))
    try:
      l.get_contents_to_filename(d)
    except OSError:
      if not os.path.exists(d):
        os.makedirs(d)  # creation of the directory with the name passed in LOCAL_PATH

downloadArq(bucket)
