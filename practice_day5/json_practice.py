import json

data = {"name": "Tien Dat", "role": "Backend", "skills": ["Python", "Linux"]}
chuoi_json=json.dumps(data, indent=4)
print(chuoi_json)