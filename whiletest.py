import time
import parseData
import send_discord
import getinfo
import eewimage

prevquake = {}
prevquake["report_num"] = "0"
prevquake["report_id"] = "0"
PrevID = ""


while(True):
    quakedata = getinfo.GetEEWfromMonitor()
    if(quakedata["result"]["message"] == ""):
        if((quakedata['report_id'] != prevquake['report_id']) or (int(quakedata["report_num"]) > int(prevquake["report_num"]))):
            Info = getinfo.GetEEWfromMonitor()
            base,layer = getinfo.GetEewImage()
            payload,file= parseData.formatEewData(Info,eewimage.generateEewImage(base,layer))
            send_discord.sendDiscord(payload,file)
    prevquake = quakedata
    print(f"loop{getinfo.timestring()}")
    time.sleep(10)
                    