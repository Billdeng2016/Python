# coding:utf-8
import requests
import json
data = {
    'managerName':'admin',
    'managerPwd':'lian1202',
    'captchaId':'23551219',
    'captcha':'xqvz'
}
url = 'https://www.imooc.com/index/getstarlist'


class RunMain:
    def __init__(self):
        self.res = None

    def send_get(self, url, data):
        # 将json转换成dict
        self.res = requests.get(url=url).json()
        # print(type(res))
        # 增加缩进和排序
        self.res = json.dumps(self.res,indent=2,sort_keys=False)
        # return self.res

    def send_post(self,url,data):
        self.res = requests.post(url=url,data=data).json()
        print(type(self.res))
        self.res = json.dumps(self.res,indent=2,sort_keys=False)
        # return self.res

    def run_main(self,url,method,data=None):
        if method == 'GET':
            self.send_get(url, data)
        else:
            self.send_post(url.data)
        return self.res



#if __name__ == '__main__':
    #run = RunMain(url,'GET')
    #print(run.res)


