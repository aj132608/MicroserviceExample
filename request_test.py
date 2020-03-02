import requests

if __name__ == "__main__":
    url = 'http://127.0.0.1:8080/post-example'
    json_message = {
        "message": "hello",
        "author": "Alex Jirovsky"
    }

    response = requests.post(url=url,
                             json=json_message)

    status_code = response.status_code
    response_body = response.text

    print(f"status code: {status_code}")
    print(f"response: {response_body}")
