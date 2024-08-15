import requests
import sys
import os

url = 'http://localhost:8000/fileupload/'

file_path = sys.argv[1]

if not os.path.exists(file_path):
    print(f"Error: The file '{file_path}' does not exsist.")
    sys.exit(1)
    
if os.path.isdir(file_path):
    print(f"Error: '{file_path}' is not a file.")
    sys.exit(1)


file_name = os.path.basename(file_path)

with open(file_path, 'rb') as file:
    files = {
        'file': (file_name, file, 'application/pdf')
    }

    response = requests.post(url, files=files)


if response.status_code == 200:
    print('Upload succesfull')
else:
    print(f'Error during file upload: {response.status_code}, {response.json()['detail']}')
