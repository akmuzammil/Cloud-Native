from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

#added endpoint for metrics 
#usage: http://localhost:5000/metrics
@app.route("/metrics")
def getMetrics():
    
    app.logger.debug("metrics endpoint was reached")
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    return response


#added endpoint for status 
#usage: http://localhost:5000/status
@app.route("/status")
def getStatus():
     app.logger.debug("status endpoint was reached")

     response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
     return response

if __name__ == "__main__":
    logging.basicConfig(filename="app.log",level=logging.DEBUG,
                    format='%(asctime)s %(message)s',filemode='w')
    app.run(host='0.0.0.0')
    