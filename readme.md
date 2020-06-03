NextWord
===
steps to run

1. start the machine learning backend 
```env FLASK_APP=backend.py flask run --port 8050```
2. host the flaskapp.py using apache 2 

Notes:
- the ip for the machine learning backend is hard coded
- setup for the apache server is not documented but guides online should be able to help
    - https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/