import requests

url = "https://icanhazdadjoke.com/search"


res = requests.get(
  url,
  headers={"Accept": "application/json"},
  params = {"term": "boop"}

)

data = res.json()

print(len(data['results']))
