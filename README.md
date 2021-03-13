# Lunchtimeapi
Backend API service for Lunchtime IO, following microservices architecture

Each of these services should run on a AWS Lambda instance.

## Deployment to AWS Lambda
Initialize your deployment by creating a new virtual environment on the folder
<code> virtualenv .env </code> 

Activate your environment, and run a pip install

<code> pip install -r requirements.txt </code> 

Once done, set your region in the Zappa config and run:

<code> zappa init </code> 

Follow through onboarding and then deploy: 

<code> zappa deploy [YOUR ENVIRONMENT SUCH AS DEV] </code>

To update, run: 

<code> zappa update [YOUR ENVIRONMENT SUCH AS DEV] </code>

## Deployment to AWS EC2
Utility files are services which can be deployed to EC2 and run Chronjobs to automate jobs like clearing counters etc.
