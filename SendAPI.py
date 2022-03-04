import requests

targetIP = "127.0.0.1:5000"
data = "8888"

def sendGet():
    url = f'http://{targetIP}/setString'
    url = f'{url}?data={data}'
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print(r.text)

def sendPost():
    url = f'http://{targetIP}/setString'
    my_data = {'data': data}
    r = requests.post(url, data = my_data)
    if r.status_code == requests.codes.ok:
        print(r.text)


if __name__=="__main__":
    # sendGet()
    sendPost()
