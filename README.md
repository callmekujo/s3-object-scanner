# S3 Object Scanner
This tool is to scan all your S3 buckets and their objects to determine which objects are publicly accessible. There are many S3 bucket scanners out there that will simply tell you if an S3 bucket itself is public or not. These scanners typically do not take into consideration of object ACLs. While an S3 bucket may be open, the objects inside can remain non-public; or vice-versa. This tool solves that problem by pulling the object ACL into a CSV file to be later reviewed. 

## Goal of this tool
Identify objects within your S3 buckets that are pubicly accessible. While an S3 bucket itself may not be publicly accessible, this does not mean the objects immediately inherit that same viewership. This tool will output a CSV file that dumps all your buckets, objects, and their respective policies. 

## How to use
1. Create necessary permissions to perform this task. You can accomplish this with roles or user groups, a IAM user and a security credential. 
   - Whether you choose to use a role or user group, is up to you. I recommend making a policy that only allows interactions with your S3 buckets and nothing else. 
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "hackathon",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketPublicAccessBlock",
                "s3:GetObjectAcl",
                "s3:GetObject",
                "s3:ListAllMyBuckets",
                "s3:GetBucketLogging",
                "s3:GetObjectAttributes",
                "s3:ListBucket",
                "s3:GetBucketAcl",
                "s3:GetBucketPolicy"
            ],
            "Resource": "*"
        }
    ]
}
```