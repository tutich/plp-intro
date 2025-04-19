import requests as req

response = req.get('https://api.github.com/events')
print(response.status_code)  # 200
print(response.json())  # JSON response