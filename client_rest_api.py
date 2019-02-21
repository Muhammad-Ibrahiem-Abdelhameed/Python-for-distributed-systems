import sys
import json
import requests
import fileinput
res = requests.get('http://127.0.0.1:5000/')
print(res.content)

print("===================")
student = requests.get('http://127.0.0.1:5000/student').json()
print(student)

print("===================")
res_file = requests.get('http://127.0.0.1:5000/file', stream=True)
with open('ff.pptx', 'wb') as f:
    f.write(res_file.content)

print(type(res_file.content))