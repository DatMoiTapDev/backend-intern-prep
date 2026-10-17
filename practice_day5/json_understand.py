import json
api_response = '{"server": "nginx", "status": 200, "active": true}'
du_lieu_python = json.loads(api_response)
print(du_lieu_python["status"])