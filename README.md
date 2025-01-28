# cli-test
This python cli based on Click deploy, update and rollback flask app using ansible

the build and push of the docker image done by python docker module

# Prerequisites
1. run ```python -m venv venv && source venv/bin/activate```
2. run ```pip install -r requirements.txt```
3. docker should be installed

# Usage
  to see cli options run ```python cli.py --help```. the output will be
```
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --config PATH  [required]
  --env TEXT     [required]
  --verbose
  --log PATH
  --secret TEXT
  --help         Show this message and exit.

Commands:
  deploy
  rollback
  update
```
to define secret run ```export secret=<secret>``` on shell

# Deploy
to deploy the app run ```python cli.py --config config.ini --env dev --secret=$secret deploy```  
after the run finished you should open http://localhost:5000 and see ```Hello, Flask!```  

# Update
to update the app make some changes on app.py, for example change ```Hello, FLask!``` to ```Hello, Flask!!!```  
update the tag on config.ini to v2  
run ```python cli.py --config config.ini --env dev --secret=$secret update```  
after the run finished you should see on http://localhost:5000 ```Hello, Flask!!!```
 
# Rollback
to rollback the app change the tag on config.ini to v1  
and run ```python cli.py --config config.ini --env dev --secret=$secret rollback```  
you should see ```Hello, Flask!``` back
 
# Troubleshooting
the app writes by default to cli.log

example:
  
    2025-01-28 08:25:40,598 - root - INFO - Starting deployment process
    2025-01-28 08:25:40,598 - root - INFO - Building Docker image flask_app:v1 from app
    2025-01-28 08:25:52,056 - root - INFO - Docker image flask_app:v1 built successfully
    2025-01-28 08:25:52,057 - root - INFO - Pushing Docker image flask_app:v1
    2025-01-28 08:25:52,057 - root - INFO - Docker image flask_app:v1 pushed successfully
    2025-01-28 08:25:54,371 - root - INFO - Deployment process completed
