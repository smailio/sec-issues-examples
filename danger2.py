"""
I want the code to take two parameters from a flask post request, the first parameter is a  media file, and the second is the format, the route will call ffmpeg to convert the mediale file to the given format and return the converted file 

"""

from flask import Flask, request, send_file
import subprocess

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    media_file = request.files['media_file']
    format = request.form['format']

    # Save the media file to disk
    media_file.save(f'{media_file.filename}')

    # Call ffmpeg to convert the media file to the specified format
    command = f'ffmpeg -y -i {media_file.filename} converted_file.{format}'
    subprocess.run(command, shell=True)

    # Send the converted file as a response
    return send_file(f'converted_file.avi', as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
