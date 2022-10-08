#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..')
from base.spider import Spider
import json

class Spider(Spider):
    def getName(self):
        return "百影视频"
    def init(self,extend=""):
        print("============{0}============".format(extend))
        pass
    def homeContent(self,filter):
        result = {}
        cateManual = {
            "电视剧":"2",
            "电影":"1",
            "综艺":"3",
            "动漫":"4"
        }
        classes = []
        for k in cateManual:
            classes.append({
                'type_name':k,
                'type_id':cateManual[k]
            })

        result['class'] = classes
        return result
    def homeVideoContent(self):
        rsp = self.fetch("https://api.8a5.cn/parse/baiying/py.php?do=homeVideoContent")
        alists = json.loads(rsp.text)
        alist = alists['list']
        result = {
            'list':alist
        }
        return result
    def categoryContent(self,tid,pg,filter,extend):
        result = {}
        urlParams = []
        params = ''
        for key in extend:
            urlParams.append(str(key) + '=' + extend[key])
        params = '&'.join(urlParams)
        url = 'https://api.8a5.cn/parse/baiying/py.php?do=categoryContent&tid={0}&page={1}&{2}'.format(tid, pg,params)
        rsp = self.fetch(url)
        alists = json.loads(rsp.text)
        alist = alists['list']

        result['list'] = alist
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self,array):
        tid = array[0]
        url = 'https://api.8a5.cn/parse/baiying/py.php?do=detailContent&id={0}'.format(tid)
        rsp = self.fetch(url)
        alists = json.loads(rsp.text)
        vod = alists['vod']
        result = {
            'list':[
                vod
            ]
        }
        return result

    def searchContent(self,key,quick):
        url = 'https://api.8a5.cn/parse/baiying/py.php?do=searchContent&wd={0}'.format(key)
        rsp = self.fetch(url)
        alists = json.loads(rsp.text)
        list = alists['list']
        result = {
            'list':list
        }
        return result


    def playerContent(self,flag,id,vipFlags):
        result = {}
        if 'api.8a5.cn' in id:
            rsp = self.fetch(id)
            alists = json.loads(rsp.text)
            id = alists['url']
        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = id
        return result

    def isVideoFormat(self,url):
        pass
    def manualVideoCheck(self):
        pass
    def localProxy(self,param):
        return [200, "video/MP2T", action, ""]
