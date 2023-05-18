import web
import requests
import jsonpath
import json
import random
import time
import html
#import pymysql 后续功能使用
#import datetime 后续功能使用
#import threading 后续功能使用

#说明：本项目修改自Claude_gptyier开源项目，我们添加了一些功能.原项目地址：https://github.com/oaskdosakdoakd/Claude_gptyier
# 全局配置
to = "" # Slack工作区对话Token
coo = "" # Cookie
userid = "" # 用户ID
fjid = "" # 房间ID

urls = (
    '/', 'gpt',
    '/setsession', 'setsession',
    '/stream', 'stream',
    '/css/(.*)', 'static_handler_css',
    '/js/(.*)', 'static_handler_js',
    '/black','black_g',
)

headers = {
        'Host': 'yierco.slack.com',
        'Cookie': coo
    }

token=to

Claude_userid=userid
fangjian_id=fjid

app = web.application(urls, globals())
app.debug = False
render = web.template.render('templates')

#————待开发的功能，勿动————
#新功能：访问次数限制
'''
def reset_access_logs():
    today = datetime.date.today()
    with db.cursor() as cursor:
        cursor.execute("DELETE FROM access_logs WHERE date < %s", (today,))
        db.commit()

# 设置MySQL数据库连接信息
db = pymysql.connect(host='localhost',
                     user='chat',
                     password='123456',
                     db='chat',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

# 创建访问记录表格
with db.cursor() as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS access_logs (ip_address VARCHAR(255), count INT, date DATE)")
    db.commit()

# 记录访问IP地址的函数，如果请求中带有?admin=true参数，则不记录访问计数
def log_ip_address(ip_address, admin):
    if admin:
        return None

    # 获取今天的日期
    today = datetime.date.today()

    # 查询是否有以前的记录，如果没有则插入新记录
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM access_logs WHERE ip_address = %s AND date = %s", (ip_address, today))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO access_logs (ip_address, count, date) VALUES (%s, %s, %s)", (ip_address, 1, today))
        else:
            # 如果有以前的记录，则更新访问计数
            count = result['count'] + 1
            cursor.execute("UPDATE access_logs SET count = %s WHERE ip_address = %s AND date = %s", (count, ip_address, today))
        
        # 提交更改
        db.commit()

        # 获取今天的访问计数
        cursor.execute("SELECT COUNT(*) as count FROM access_logs WHERE date = %s", (today,))
        count = cursor.fetchone()['count']

        # 如果访问计数超过10，则返回“已超额，请明日访问”
        if count > 10:
            return "已超额，请明日访问"
# 每天0点重置访问计数的定时器
def schedule_reset_access_logs():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    if now < midnight:
        # 如果现在还没到0点，则等到0点后再重置访问计数
        delay = (midnight - now).total_seconds()
        threading.Timer(delay, reset_access_logs).start()
    else:
        # 如果已经过了0点，则立即重置访问计数
        reset_access_logs()
        # 然后等待到明天0点再重置访问计数
        delay = (midnight + datetime.timedelta(days=1) - now).total_seconds()
        threading.Timer(delay, schedule_reset_access_logs).start()

# 启动每天0点重置访问计数的定时器
schedule_reset_access_logs()

'''
#————END————
class gpt:
    def GET(self):
        web.header('Content-Type', 'text/html; charset=utf-8')
        with open('gpt.html', 'r',encoding='utf-8') as file:
            html_content = file.read()
        return html_content
class black_g:
    def GET(self):
        web.header('Content-Type', 'text/html; charset=utf-8')
        with open('black_g.html', 'r',encoding='utf-8') as file:
            html_content = file.read()
        return html_content



class static_handler_css:
    def GET(self, filename):
        try:
            with open(f'css/{filename}', 'rb') as f:
                return f.read()
        except FileNotFoundError:
            raise web.notfound("File not found")
class static_handler_js:
    def GET(self, filename):
        try:
            with open(f'js/{filename}', 'rb') as f:
                return f.read()
        except FileNotFoundError:
            raise web.notfound("File not found")

class setsession:

    def POST(self):
        if 1 > 2:
            pass
        else:
    
            stream_url_post_postMessage_r_json_ts = web.cookies().get('ts')
            url_conversations_replies_huoqu_latest_reply_json_latest_reply2 = web.cookies().get('latest_reply')
    
    
            setsession_data = web.input(message=None)
            message = setsession_data.message
    
    
            message=message.replace("\"", '\\\"')
    
            print(message)
    
            prompt=message
    
    
            url_post_postMessage = 'https://yierco.slack.com/api/chat.postMessage'
    
            if(url_conversations_replies_huoqu_latest_reply_json_latest_reply2!=None):
                url_post_postMessage_file = {
                    'token': (None,
                              token,
                              None),
                    'channel': (None, '{}'.format(fangjian_id), None),
                    'ts': (None, '1681546073.xxxxx5', None),
                    'type': (None, 'message', None),
                    'reply_broadcast': (None, 'false', None),
                    'thread_ts': (None, '{}'.format(stream_url_post_postMessage_r_json_ts), None),
                    'unfurl': (None, '[]', None),
                    'blocks': (None,
                               '[{"type":"rich_text","elements":[{"type":"rich_text_section","elements":[{"type":"user","user_id":"%s"},{"type":"text","text":" %s"}]}]}]' % (
                                   Claude_userid,prompt), None),
                    'include_channel_perm_error': (None, 'true', None),
                    '_x_reason': (None, 'webapp_message_send', None),
                    '_x_mode': (None, 'online', None),
                    '_x_sonic': (None, 'true', None)
                }
            else:
                url_post_postMessage_file = {
                    'token': (None,
                              token,
                              None),
                    'channel': (None, '{}'.format(fangjian_id), None),
                    'ts': (None, '1681546073.xxxxx5', None),
                    'type': (None, 'message', None),
                    'unfurl': (None, '[]', None),
                    'blocks': (None,
                               '[{"type":"rich_text","elements":[{"type":"rich_text_section","elements":[{"type":"user","user_id":"%s"},{"type":"text","text":" %s"}]}]}]' % (
                                   Claude_userid,prompt), None),
                    'include_channel_perm_error': (None, 'true', None),
                    '_x_reason': (None, 'webapp_message_send', None),
                    '_x_mode': (None, 'online', None),
                    '_x_sonic': (None, 'true', None)
                }
    
            try:
                url_post_postMessage_r = requests.post(url_post_postMessage, headers=headers,
                                                   files=url_post_postMessage_file, verify=False)
    
            except BaseException as e:
                print("查询失败,正在重试")
                print(e)
                for o in range(100):
                    try:
                        url_post_postMessage_r = requests.post(url_post_postMessage, headers=headers,
                                                               files=url_post_postMessage_file, verify=False)
                        if url_post_postMessage_r.status_code == 200:
                            break
                    except BaseException as e:
                        print("再次查询子域名失败", o)
                        print(e)
    
            if ("\"ok\":true" in url_post_postMessage_r.text and "thread_ts" in url_post_postMessage_r.text and url_conversations_replies_huoqu_latest_reply_json_latest_reply2!=None):
                url_post_postMessage_r_json = json.loads(url_post_postMessage_r.text)
                url_post_postMessage_r_json_thread_ts = jsonpath.jsonpath(url_post_postMessage_r_json, "$.message.thread_ts")[0]
    
                url_post_postMessage_r_json_ts = jsonpath.jsonpath(url_post_postMessage_r_json, "$.ts")[0]
                web.setcookie('ts', '{}'.format(url_post_postMessage_r_json_thread_ts), 36000)
                web.setcookie('thread_ts', '{}'.format(url_post_postMessage_r_json_ts), 36000)
    
    
                return '{"success":true}'
            elif ("\"ok\":true" in url_post_postMessage_r.text and url_conversations_replies_huoqu_latest_reply_json_latest_reply2==None):
                url_post_postMessage_r_json = json.loads(url_post_postMessage_r.text)
                url_post_postMessage_r_json_ts = jsonpath.jsonpath(url_post_postMessage_r_json, "$.ts")[0]
                web.setcookie('ts', '{}'.format(url_post_postMessage_r_json_ts), 36000)
    
                return '{"success":true}'
            else:
                return '{"success":false}'


class stream:
    def GET(self):
        if 1 > 2:
            pass
        else:
    
            stream_url_post_postMessage_r_json_ts = web.cookies().get('ts')
            # url_conversations_replies_huoqu_latest_reply_json_latest_reply2 = web.cookies().get('latest_reply')
            url_post_postMessage_r_json_thread_ts = web.cookies().get('thread_ts')
    
            url_conversations_replies = 'https://yierco.slack.com/api/conversations.replies'
    
    
            for i in range(120):
                try:
                    url_conversations_replies_file = {
                        'token': (None,
                                  token,
                                  None),
                        'channel': (None, '{}'.format(fangjian_id), None),
                        'ts': (None, '{}'.format(stream_url_post_postMessage_r_json_ts), None),
                        'inclusive': (None, 'ture', None),
                        'limit': (None, '28', None),
                        'oldest': (None, '{}'.format(stream_url_post_postMessage_r_json_ts), None),
                        '_x_reason': (None, 'history-api/fetchReplies', None),
                        '_x_mode': (None, 'online', None),
                        '_x_sonic': (None, 'true', None)
                    }
                    url_conversations_replies_huoqu_latest_reply = requests.post(url_conversations_replies, headers=headers,
                                                            files=url_conversations_replies_file, verify=False)
                except BaseException as e:
                    print("查询失败,正在重试")
                    print(e)
                    for o in range(100):
                        try:
                            url_conversations_replies_huoqu_latest_reply = requests.post(url_conversations_replies, headers=headers,
                                                                        files=url_conversations_replies_file,
                                                                        verify=False)
                            if url_conversations_replies_huoqu_latest_reply.status_code == 200:
                                break
                        except BaseException as e:
                            print("再次查询子域名失败", o)
                            print(e)
    
                if(i>2 and "latest_reply" not in url_conversations_replies_huoqu_latest_reply.text and "thread_ts" not in url_conversations_replies_huoqu_latest_reply.text):
                    web.header('Content-Type', 'text/event-stream')
                    web.header('Access-Control-Allow-Origin', '*')
                    web.header('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
                    web.header('Pragma', 'no-cache')
                    return """data: {"id":"chatcmpl-75nIQFpIpwE3zjcpga0VGgULV3Lyh","object":"chat.completion.chunk","created":1681615490,"model":"gpt-3.5-turbo-0301","choices":[{"delta":{"content":"%s"},"index":0,"finish_reason":null}]}
    
    
                                data: [DONE]
    
                                """ % ("错误")
    
                #print(url_conversations_replies_huoqu_latest_reply.text)
                if ("\"ok\":true" in url_conversations_replies_huoqu_latest_reply.text and "latest_reply" in url_conversations_replies_huoqu_latest_reply.text and "thread_ts" in url_conversations_replies_huoqu_latest_reply.text):
    
                    url_conversations_replies_huoqu_latest_reply_json = json.loads(url_conversations_replies_huoqu_latest_reply.text)
    
                    url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply = jsonpath.jsonpath(url_conversations_replies_huoqu_latest_reply_json, "$.messages[0].latest_reply")[0]
    
                    #print("url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply:{}".format(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply))
                    #print("url_post_postMessage_r_json_thread_ts:{}".format(url_post_postMessage_r_json_thread_ts))
    
                    if(url_post_postMessage_r_json_thread_ts!=url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply and url_post_postMessage_r_json_thread_ts!=None):
                        #print(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply)
                        web.setcookie('latest_reply', '{}'.format(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply), 36000)
                        break
    
                    elif(url_post_postMessage_r_json_thread_ts==None):
                        #print(url_post_postMessage_r_json_thread_ts)
                        web.setcookie('latest_reply',
                                      '{}'.format(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply),
                                      36000)
                        break
                else:
                    time.sleep(0.2)
            # url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply = web.cookies().get('latest_reply')
    
    
            if(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply!=None):
                for i in range(120):
                    try:
                        url_conversations_replies_file2 = {
                            'token': (None,
                                      token,
                                      None),
                            'channel': (None, '{}'.format(fangjian_id), None),
                            'ts': (None, '{}'.format(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply), None),
                            'inclusive': (None, 'ture', None),
                            'limit': (None, '28', None),
                            'oldest': (None, '{}'.format(url_conversations_replies_huoqu_latest_reply_json_messages_latest_reply), None),
                            '_x_reason': (None, 'history-api/fetchReplies', None),
                            '_x_mode': (None, 'online', None),
                            '_x_sonic': (None, 'true', None)
                        }
                        url_conversations_replies_r = requests.post(url_conversations_replies, headers=headers,
                                                                files=url_conversations_replies_file2, verify=False)
                    except BaseException as e:
                        print("查询失败,正在重试")
                        print(e)
                        for o in range(100):
                            try:
                                url_conversations_replies_r = requests.post(url_conversations_replies, headers=headers,
                                                                            files=url_conversations_replies_file2,
                                                                            verify=False)
                                if url_conversations_replies_r.status_code == 200:
                                    break
                            except BaseException as e:
                                print("再次查询子域名失败", o)
                                print(e)
    
                    # print(url_conversations_replies_r.text)
                    if(i>2 and "_Typing" not in url_conversations_replies_r.text and "thread_ts" not in url_conversations_replies_r.text):
                        web.header('Content-Type', 'text/event-stream')
                        web.header('Access-Control-Allow-Origin', '*')
                        web.header('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
                        web.header('Pragma', 'no-cache')
                        return """data: {"id":"chatcmpl-75nIQFpIpwE3zjcpga0VGgULV3Lyh","object":"chat.completion.chunk","created":1681615490,"model":"gpt-3.5-turbo-0301","choices":[{"delta":{"content":"%s"},"index":0,"finish_reason":null}]}\n\n\ndata: [DONE]\n\n"""% ("错误")
    
                    if ("\"ok\":true" in url_conversations_replies_r.text and "_Typing" not in url_conversations_replies_r.text and "thread_ts" in url_conversations_replies_r.text):
                        url_conversations_replies_r_json = json.loads(url_conversations_replies_r.text)
                        url_conversations_replies_r_json_text = jsonpath.jsonpath(url_conversations_replies_r_json, "$.messages[0].text")[0]
    
                        url_conversations_replies_r_json_text=html.unescape(url_conversations_replies_r_json_text).replace("\n","\\\\n").replace("\"","\\\"")
    
                        break
                    else:
                        time.sleep(1)
                else:
                    web.header('Content-Type', 'text/event-stream')
                    web.header('Access-Control-Allow-Origin', '*')
                    web.header('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
                    web.header('Pragma', 'no-cache')
                    return """data: {"id":"chatcmpl-75nIQFpIpwE3zjcpga0VGgULV3Lyh","object":"chat.completion.chunk","created":1681615490,"model":"gpt-3.5-turbo-0301","choices":[{"delta":{"content":"%s"},"index":0,"finish_reason":null}]}\n\n\ndata: [DONE]\n\n"""% ("错误")
    
                #print(url_conversations_replies_r_json_text)
                web.header('Content-Type', 'text/event-stream')
                web.header('Access-Control-Allow-Origin', '*')
                web.header('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
                web.header('Pragma', 'no-cache')
                return """data: {"id":"chatcmpl-75nIQFpIpwE3zjcpga0VGgULV3Lyh","object":"chat.completion.chunk","created":1681615490,"model":"gpt-3.5-turbo-0301","choices":[{"delta":{"content":"%s"},"index":0,"finish_reason":null}]}\n\n\ndata: [DONE]\n\n"""%(url_conversations_replies_r_json_text)


if __name__ == "__main__":
    print("本程序由Claude_gptyier项目修改而来，由 AZ Studio二次开发")
    app.run()
