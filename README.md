# MedWatch
MedWatch is a remote patient monitoring system. I started this personal project as a solo participant in the 2021 Yale CBIT Hackathon.

I designed and developed this personal project using AWS technologies. Some of the AWS services I used are AWS IoT, Lambda, API Gateway, Kinesis Firehose, S3, and QuickSight to handle, store, and visualize incoming medical sensor data which was simulated using AWS Boto3 Python package and AWS CLI. Throughout this project I used S3 lifecycle policies to handle archiving of data and IAM roles to allocate just enough permissions for AWS resources. 

I provisioned all resources from the AWS Management console. As a best practice, I created a new IAM user with admin access privileges and provisioned resources from there instead of doing everything from the root user account. 

After running the demo script which simulated medical sensors, you can see the patient dashboard update as data is recieved in real-time. Just head over to this static webpage, hosted in an S3 bucket: https://patientmonitoringvishva2021.s3.amazonaws.com/patientMonitor.html

Send questions to "vishvanata@gatech.edu".
