# Data-Sync-Service
This Python script continuously fetches data from a database and updates a Redis List with data and timestamps. It allows you to keep track of when data was synced to Redis.

## Prerequisites
- Python (3.6+)
- MySQL Server
- Redis server

## Deployment
- For Deployment, create a wheel package that deploys in the site-packages directory.
- So, first need to run setup.py
- It will generate a wheel package in dist dir.
- We can install the wheel package locally by using the following command
    $pip install dist/datasync-0.0.1-py3-none-any.whl

## Run Package
- After installing, we can directly run the package.
- We can run the package by using python command with `-m` flag.
    $python -m datasync.main

# Architecture 

![user_service (1)](https://github.com/shantanukrshukla/Data-Sync-Service/assets/147392084/ee979913-0aff-4d03-a53b-d357191a3878)
