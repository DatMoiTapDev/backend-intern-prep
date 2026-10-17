import os
os.environ["MY_SECRECT_TOKEN"]="abc-123-xyz"
token = os.getenv("MY_SECRECT_TOKEN")
print(f"Token lấy từ hệ điều hành là: {token}")