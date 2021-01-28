import requests
import codecs

def apiGet():
    response = requests.get("http://localhost:1337/meteos")
    return response.text

def fileSave(data):
    with codecs.open("backup.json", 'w', encoding='utf8') as f:
        f.write(data)
    f.close()

fileSave(apiGet())