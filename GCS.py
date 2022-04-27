from google.cloud import storage
# Setting credentials using the downloaded JSON file

client = storage.Client.from_service_account_json(json_credentials_path='privatekey.json')

#creating a new bucket
bucket_name = 'insertBucketNameHere'
bucket = client.bucket(bucket_name)
bucket.location = 'US'
bucket = client.create_bucket(bucket)

# Creating bucket object
bucket = client.get_bucket('insertBucketNameHere')

# Name of the object to be stored in the bucket
object_name_in_gcs_bucket = bucket.blob('prod.csv')

# Name of the object in local file system
object_name_in_gcs_bucket.upload_from_filename('products.csv')