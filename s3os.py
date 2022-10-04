import boto3
import logging
from botocore.exceptions import ClientError
import csv
from csv import writer

# Create session for scanner using known AWS configure profile "hackathon"
session = boto3.Session(profile_name='replace-me')
hackathon = session.client('s3')

# Header for CSV
csv_header = ['bucket', 'bucket_acl', 'object', 'object_acl']
# Retrieve the list of existing buckets
ls_buckets = hackathon.list_buckets()
# Output the bucket names
print('Existing buckets:')
with open('buckets.csv', 'w', newline='', encoding='UTF8') as buckets_csv:
    csv_write_header = csv.DictWriter(buckets_csv, fieldnames=csv_header)
    csv_write_header.writeheader()
    for bucket in ls_buckets['Buckets']:
        print(f'{bucket["Name"]}')
        # Output bucket ACL
        bucket_acl = hackathon.get_bucket_acl(
            Bucket=bucket["Name"]
        )
        write_buckets = csv.writer(buckets_csv)
        write_buckets.writerow({bucket["Name"]})
        for acl in bucket_acl['Grants']:
            print(f'{acl}')

        # Output objects from each bucket
        ls_objects = hackathon.list_objects_v2(
            Bucket=bucket["Name"]
        )
        try: 
            for objects in ls_objects['Contents']:
                print(f'{objects["Key"]}')
                # Output object ACL
                object_acl = hackathon.get_object_acl(
                    Bucket=bucket["Name"],
                    Key=objects["Key"]
                )
                print(f'{object_acl["Grants"]}')
                write_data = csv.writer(buckets_csv)
                write_data.writerow(['', bucket_acl['Grants'], objects["Key"], object_acl["Grants"]])
        except KeyError:
            print('No objects found in bucket')