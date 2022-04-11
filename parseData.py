from codecs import getincrementaldecoder
from datetime import  datetime
import xml.etree.ElementTree as et

def intensity_image(intensity):
    url = "https://api.yukineko.me/eewp/v3/sindo/{}"
    if intensity == "7":
        image_url = url.format(9)
        return image_url
    if intensity == "6強":
        image_url = url.format(8)
        return image_url
    if intensity == "6弱":
        image_url = url.format(7)
        return image_url
    if intensity == "5強":
        image_url = url.format(6)
        return image_url
    if intensity == "5弱":
        image_url = url.format(5)
        return image_url
    if intensity == "4":
        image_url = url.format(4)
        return image_url
    if intensity == "3":
        image_url = url.format(3)
        return image_url
    if intensity == "2":
        image_url = url.format(2)
        return image_url
    if intensity == "1":
        image_url = url.format(1)
        return image_url

def generate_title(Data):
    if Data['is_final'] == True:
        title = "地震情報 最終報"
    else:
        title = f"地震情報 第{Data['report_num']}報"
    return title

def convert_time(str):
    time_dt = datetime.strptime(str,'%Y%m%d%H%M%S')
    time = datetime.strftime(time_dt,'%Y/%m/%d %H:%M:%S')
    return time

def formatEewData(eewData,eewImage):
    title = generate_title(eewData)
    payload = {
        "payload_json" :{
                "embeds": [{
                    "title": title,
                    "thumbnail": {
                        "url": intensity_image(eewData["calcintensity"])
                        },
                    "image": {
                        "url": "attachment://eewImage.png"
                    },
                    "description" : f"**更新時刻:{convert_time(eewData['request_time'])}**",
                    "url": "http://www.kmoni.bosai.go.jp/",
                    "fields": [{
                        "name":"震央",
                        "value": eewData['region_name'],
                        "inline": True
                    },
                    {
                        "name": "発生時刻",
                        "value": convert_time(eewData['origin_time']),
                        "inline": True
                    },
                    {
                        "name": "予想最大震度",
                        "value": eewData['calcintensity'],
                        "inline": True
                    },
                    {
                        "name": "マグニチュード",
                        "value": eewData['magunitude'],
                        "inline": True
                    },
                    {
                        "name": "深さ",
                        "value": eewData['depth'],
                        "inline": True
                    },
                    {
                        "name" : "形式",
                        "value": eewData['alertflg'],
                        "inline": True
                    }]
                }]
            }
        }
    file = {
        "image": ("eewImage.png",eewImage)
    }
    return payload,file

def formatNHKData(NHKInfoXML):
    Root = NHKInfoXML
    payload = {
            "embeds":[{
                "title": "NHK地震情報",
                "description": f"**更新時刻:{Root[0].text}**",
                "url": "https://www.nhk.or.jp/kishou-saigai/earthquake/",
                "image":{
                    "url": f"https://www3.nhk.or.jp/sokuho/jishin/{Root[1][0].text}"
                },
                "thumbnail":{
                    "url": intensity_image(Root[1].attrib['Intensity'])
                },
                "fields":[{
                    "name": "震央",
                    "value": Root[1].attrib['Epicenter'],
                    "inline": True
                },
                {
                    "name": "発生時刻",
                    "value": Root[1].attrib['Time'],
                    "inline": True
                },
                {
                    "name": "マグニチュード",
                    "value": Root[1].attrib['Magnitude'],
                    "inline": True
                },
                {
                    "name": "深さ",
                    "value": Root[1].attrib['Depth'],
                    "inline": False
                }
                ]
        }]
    }

    return payload