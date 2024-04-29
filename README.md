How to test

RUN IN LINUX OR WSL2!
Celery does not support windows

Install requirements: pip install -r requirements.txt
Versions are the same as aspose-total-net installs, due to confusing packaging and dependency issues. 

Make sure redis is either installed locally and running on port 6379 or start it using the provided docker-compose file

Make sure libssl1 is installed 
(Ubuntu 22.04: wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1-1ubuntu2.1~18.04.23_amd64.deb && dpkg -i libssl1.1_1.1.1-1ubuntu2.1~18.04.23_amd64.deb)
Make sure libgdiplus is installed

Start celery worker process: celery -A tasks worker --loglevel=INFO
