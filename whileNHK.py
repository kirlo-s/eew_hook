import parseData
import send_discord
import getinfo
import time 


send_discord.sendRestartMessage()

PrevID = ""
while(True):
    NHKInfo = getinfo.getNHKQuakeInfo()
    QuakeID = NHKInfo[1].attrib['Id']
    if(QuakeID != PrevID):
        payload = parseData.formatNHKData(NHKInfo)
        send_discord.sendDiscordNoFiles(payload)
    PrevID = QuakeID
    print(f"loop{getinfo.timestring()}")
    time.sleep(600)
