import requests

# getting directories from list
f = open('dirlist.txt','r')
data = f.read().split('\n')
f.close()
f = open('extensions.txt','r')
ex = f.read().split('\n')
f.close()

url = input("Enter URL(https://example.com/): ")

for i in data:
    for j in ex:
        url1 = url+i+j
        response = requests.get(url1)
        print(url1+"    "+str(response.status_code))
        if response.status_code != 404:
            f = open('output.txt','a')
            f.write(url1+"      "+str(response.status_code)+'\n')
            f.close()