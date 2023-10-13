# Data-Sync-Service
This Python script continuously fetches data from a database and updates a Redis List with data and timestamps. It allows you to keep track of when data was synced to Redis.

## Prerequisites
- Python (3.6+)
- MySQL Server
- Redis server

## Deployment
- For Deployment, need to create a wheel package where it deploys in the site-packages directory.
- So, first need to run setup.py
- It will generate a wheel package in dist dir.
- And we can install the wheel package locall by using the following command
    $pip install dist/datasync-0.0.1-py3-none-any.whl

## Run Package
- After installing, we can directly run the package.
- By using python command with `-m` flag, we can run the package.
    $python -m datasync.main

# Architecture 

