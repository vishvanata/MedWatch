# MedWatch
MedWatch is a remote patient monitoring system. I started this personal project as a solo participant in the 2021 Yale CBIT Hackathon.

I designed and developed this personal project using AWS technologies. Some of the AWS services I used are AWS IoT, Lambda, API Gateway, Kinesis Firehose, S3, and QuickSight to handle, store, and visualize incoming medical sensor data which was simulated using AWS Boto3 Python package and AWS CLI. Throughout this project I used S3 lifecycle policies to handle archiving of data and IAM roles to allocate just enough permissions for AWS resources. 

I provisioned all resources from the AWS Management console. As a best practice, I created a new IAM user with admin access privileges and provisioned resources from there instead of doing everything from the root user account. 

"sbs.py" is the Python script that utilizes AWS Boto3 and AWS CLI to simulate IoT data being sent to AWS IoT. To run it you'll need to download AWS CLI and then configure your AWS user. 

Here is the sample the patient dashboard which is updated as data is recieved in real-time. Head over to this static webpage, hosted in an S3 bucket, to see how the webpage looks: https://patientmonitoringvishva2021.s3.amazonaws.com/patientMonitor.html.  You'd need to copy-paste the HTML and upload it in your own S3 bucket associated with your AWS configurations and API Gateway configurations to work. You'd need your own Lambda functions and DynamoDB table to simulate IoT medical sensors in real-time, since currently what's being shown on the table is a the result of a GET request to my DynamoDB table. 

Send questions to "vishvanata@gatech.edu".
