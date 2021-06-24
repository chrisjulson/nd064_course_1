from flask import Flask
from flask import json
import logging
from werkzeug.wrappers import response

app = Flask(__name__)

@app.route('/status')
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result":"OK - Healthy"}),
        status=200,
        mimetype='application/json'
    )
    ##logging function 
    app.logger.info('Status request successful')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
    )
    ##logging function
    app.logger.info('Metrics request successfull') 
    return response

@app.route("/")
def hello():
    ## logging function 
    app.logger.info('Main request successfull')
    
    return "Hello World!"

if __name__ == "__main__":
    
    ## streaming logs to a file 
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    
    app.run(host='0.0.0.0')
