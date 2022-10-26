import requests

class Test_geturl(object):
    def __init__(self,url):
        resoponse=requests.get(url)
        print(resoponse.status_code)
        
    

if __name__=="__main__":
    Test_geturl(url)
    
