# MicroserviceExample
Example of a microservice using Docker to containerize and Python with Flask to route requests.

Run the startup.sh script to start the microservice.

```
bash startup.sh
```

Check http://localhost:8080 on your browser to confirm that it is routed to the correct port and working properly.

# Testing
If you want to run tests, run the following command to ensure that the right packages are installed.

```
pip install -r requirements.txt
```

Once you have the required packages, run request_test.py.

If everything is working, it should return a 200 status code and the dictionary that you sent it via post request.

```
status code: 200
response: {
  "message": "hello",
  "author": "Alex Jirovsky"
}
```
