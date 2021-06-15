<!-- TOC -->

- [Exercise 1](#exercise-1)
    - [Adding Endpoints](#adding-endpoints)
        - [Solution](#solution)
            - [Created Endpoints](#created-endpoints)
            - [Added json response in the endpoints](#added-json-response-in-the-endpoints)
                - [Status Endpoint](#status-endpoint)
                - [Metrics Endpoint](#metrics-endpoint)
                - [Metrics Endpoint](#metrics-endpoint)
        - [Adding Application Logging](#adding-application-logging)
            - [Initialize Logging](#initialize-logging)
            - [Log Messages](#log-messages)

<!-- /TOC -->
# Exercise 1

## Adding Endpoints
Extend the Python Flask application with /status and /metrics endpoints, considering the following requirements:

 - Both endpoints should return an HTTP 200 status code
 - Both endpoints should return a JSON response 
    ```
    e.g. {"user": "admin"}. (Note: the JSON response can be hardcoded at this stage)
    ```
 - The /status endpoint should return a response similar to this example: result: OK - healthy
 - The /metrics endpoint should return a response similar to 
    ```
    this example: data: {UserCount: 140, UserCountActive: 23}
    ```
### Solution

#### Created Endpoints
Created placeholders for endpoints 'status' and 'metrics'
```python
@app.route("/status")
def getStatus():
```

```python
@app.route("/metrics")
def getMetrics():
```

#### Added json response in the endpoints

Added below code for each endpoint

##### Status Endpoint
```python
@app.route("/status")
def getStatus():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    return response
```
##### Metrics Endpoint
```python
@app.route("/metrics")
def getMetrics():
    
    app.logger.debug("metrics endpoint was reached")
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    return response
```

#### Adding Application Logging

##### Initialize Logging
Import necessary modules for logging and add below code in main function to initialize logging to a file app.log
```python
if __name__ == "__main__":
    logging.basicConfig(filename="app.log",level=logging.DEBUG,
                    format='%(asctime)s %(message)s',filemode='w')
    app.run(host='0.0.0.0')
```

##### Log Messages
Add logging messages as shown below

```python
app.logger.debug("status endpoint was reached")
```