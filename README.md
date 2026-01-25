# MedWatch
MedWatch is a remote patient monitoring system. I started this personal project as a solo participant in the 2021 Yale CBIT Hackathon.

I designed and developed this personal project using AWS technologies. Some of the AWS services I used are AWS IoT, Lambda, API Gateway, Kinesis Firehose, S3, and QuickSight to handle, store, and visualize incoming medical sensor data which was simulated using AWS Boto3 Python package and AWS CLI. Throughout this project I used S3 lifecycle policies to handle archiving of data and IAM roles to allocate just enough permissions for AWS resources. 

I provisioned all resources from the AWS Management console. As a best practice, I created a new IAM user with admin access privileges and provisioned resources from there instead of doing everything from the root user account. 

"sbs.py" is the Python script that utilizes AWS Boto3 and AWS CLI to simulate IoT data being sent to AWS IoT. To run it you'll need to download AWS CLI and then configure your AWS user. 

