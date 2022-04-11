from io import BytesIO
import requests
from datetime import datetime
import xml.etree.ElementTree as et

def timestring():
    time = datetime.now()
    time_str = time.strftime("%Y%m%d%H%M%S")
    return time_str

def datestring():
    time = datetime.now()
    time_str = time.strftime("%Y%m%d")
    return time_str
    
def GetEEWfromMonitor():
    time = timestring()
    URL = f"http://www.kmoni.bosai.go.jp/webservice/hypo/eew/{time}.json"
    Data = requests.get(URL).json()
    return Data

def ConvertXML(URL):
    QuakeInfo = requests.get(URL)
    Tree = et.fromstring(QuakeInfo.content.decode("shift-jis"))
    return Tree

def GetEewImage():
    time=timestring()
    date=datestring()
    Base="http://www.kmoni.bosai.go.jp/data/map_img/CommonImg/base_map_w.gif"
    RealTime=f"http://www.kmoni.bosai.go.jp/data/map_img/RealTimeImg/jma_s/{date}/{time}.jma_s.gif"
    Base_Gif=BytesIO(requests.get(Base).content)
    RealTime_Gif=BytesIO(requests.get(RealTime).content)
    return Base_Gif,RealTime_Gif


def getNHKQuakeInfo():
    BASE_URL = "https://www3.nhk.or.jp/sokuho/jishin/data/JishinReport.xml"
    Root = ConvertXML(BASE_URL)
    LatestQuakeURL = Root[0][0].attrib['url']
    LatestQuake = ConvertXML(LatestQuakeURL)
    return LatestQuake
