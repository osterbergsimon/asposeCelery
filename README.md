# How to test

## In Docker
```
docker-compose build
docker-compose up
```

If actually interested in output files, make sure to set test_files as a bindmount

## Locally
* Run in Linux or WSL2 as Celery does not support windows
* Install requirements: pip install -r requirements.txt
  - Versions are the same as aspose-total-net installs, due to confusing packaging and dependency issues. 
* Make sure libssl1 is installed 
  - (Ubuntu 22.04: wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1-1ubuntu2.1~18.04.23_amd64.deb && dpkg -i libssl1.1_1.1.1-1ubuntu2.1~18.04.23_amd64.deb)
* Make sure libgdiplus is installed
* Make sure redis is either installed locally and running on port 6379 or start it using the provided docker-compose file

Start celery worker process: celery -A tasks worker --loglevel=INFO
Run with python main.py
