import json
import parseData
import send_discord
import getinfo
import eewimage

NHKInfo = getinfo.getNHKQuakeInfo()
payload = parseData.formatNHKData(NHKInfo)
send_discord.sendDiscordNoFiles(payload)