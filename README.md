# MedWatch
MedWatch is a remote patient monitoring system. 

I designed and developed this personal project using AWS technologies. Some of the AWS services I used are AWS IoT, Lambda, API Gateway, Kinesis Firehose, S3, and QuickSight to handle, store, and visualize incoming medical sensor data which was simulated using AWS Boto3 Python package and AWS CLI. Throughout this project I used S3 lifecycle policies to handle archiving of data and IAM roles to allocate just enough permissions for AWS resources. 

After running the demo script which simulated medical sensors, you can see the patient dashboard update as data is recieved in real-time. Just head over to this static webpage, hosted in an S3 bucket: https://patientmonitoringvishva2021.s3.amazonaws.com/patientMonitor.html

