aws_response = {
    "region": "ap-southeast-1",
    "instances": [
        {"id": "i-12345", "state": "running"},
        {"id": "i-67890", "state": "stopped"},
        {"id": "i-54321", "state": "running"}
    ]
}

def check_instance(aws_response):
    for res in aws_response['instances']:
        if res['state'] == 'running':
            print(f"Đang hoạt động {res['id']} ")

check_instance(aws_response)