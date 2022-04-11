import json
import requests
import webhookurl

def sendDiscord(payload,file):
    payload["payload_json"] = json.dumps(payload['payload_json'])
    res = requests.post(webhookurl.webhook,data = payload,files = file)
    print(res.status_code)
    return

def sendRestartMessage():
    msg = requests.post(webhookurl.webhook,data = json.dumps({"content":" :warning:**再起動**:warning:\r> 再起動時に最新の地震情報を表示します。\r> 発生時間は考慮されません、ご注意ください。"}),headers= {"Content-type": "application/json"})
    print(msg.status_code)
    return 

def sendDiscordNoFiles(payload):
    res = requests.post(webhookurl.webhook,data = json.dumps(payload),headers= {"Content-type": "application/json"})
    print(res.status_code)
    return
