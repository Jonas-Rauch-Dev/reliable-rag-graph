import requests

url = 'http://localhost:8000/fileupload/'

file_name = '24s-C4_Uebung_01_Angabe.pdf'

file_path = f'/home/jones/Downloads/{file_name}'

with open(file_path, 'rb') as file:
    files = {
        'file': (file_name, file, 'application/pdf')
    }

    response = requests.post(url, files=files)


if response.status_code == 200:
    print('Upload succesfull')
else:
    print(f'Error during file upload: {response.status_code}')
