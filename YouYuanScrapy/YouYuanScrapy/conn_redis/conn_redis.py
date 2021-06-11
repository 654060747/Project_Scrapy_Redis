import redis
import json
"""decode_responses 写存的数据是字符串形式"""
r = redis.StrictRedis(host='192.168.xx.xx', port=6379, password='ubuntu') # 默认db=0

def push_start_url_data(request_data):
    """
    将一个完整的request_data推送到redis的start_url列表中
    :param request_data: {'url':url, 'form_data':form_data, 'meta':meta}
    :return:
    """
    r.lpush('post_url', request_data)
 
 
if __name__ == '__main__':
    url = 'http://192.168.xx.xx:5000/test1'
    form_data = {
        "name": "狗",
        "age": "AUTO",
        "id": "AUTO",
    }
    request_data = {
        'url': url,
        'form_data': form_data
    }
    push_start_url_data(json.dumps(request_data))