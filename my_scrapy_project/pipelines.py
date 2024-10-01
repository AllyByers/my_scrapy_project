import boto3
import json

class S3Pipeline:
    def __init__(self):
        # Set up the S3 client with your credentials
        self.s3 = boto3.client(
            's3',
            aws_access_key_id='AKIAXEVXYO7YXOT4KAOS',  # Your Access Key
            aws_secret_access_key='qoTBsH2DX+1Afz9zNFZk2B5XXcmvTlaVtYd2lxdr',  # Your Secret Key
            region_name='eu-north-1'  # Your AWS region (Europe, Stockholm)
        )
        self.bucket_name = 'scrapy-output-data'  # Your S3 bucket name

    def process_item(self, item, spider):
        # Convert the item (scraped data) to JSON
        json_data = json.dumps(dict(item))
        
        # Create a unique file name for each scraped item (e.g., using the spider name and item count)
        file_name = f"{spider.name}_output.json"

        # Upload the JSON data to S3
        self.s3.put_object(
            Bucket=self.bucket_name,
            Key=file_name,
            Body=json_data
        )
        
        # Return the item to continue the Scrapy pipeline
        return item
