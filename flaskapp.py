from flask import Flask,  request,  current_app
import requests 

app = Flask(__name__)

@app.route('/')
def html():
    return current_app.send_static_file('index.html')

@app.route("/predict", methods = ['GET'])
def predict():
    text = request.args.get('text')
    URL = 'http://127.0.0.1:8050/predict'
    PARAMS = {'text':text}
    r = requests.get(url = URL, params = PARAMS) 
    return r.text
    

if __name__ == '__main__':
  app.run()
