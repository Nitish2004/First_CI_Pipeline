import requests
import subprocess

def jfrogUpload():
    url = 'http://44.201.100.155:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    file_path = '/var/lib/jenkins/workspace/DemoPipeline/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    username = 'admin'
    password = 'Nitish12'

    with open(file_path, 'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)
    
    if response.status_code == 201:
        print("\nPUT request was succesful!")
    else:
        print(f"PUT request failed with status code {response.status_code}")
        print("Response content: ")
        print(response.text)

def main():
    jfrogUpload()
