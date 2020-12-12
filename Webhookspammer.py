from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import json
import sys
wburl = sys.argv[1]
webhook = DiscordWebhook(url=wburl)

count = 0
while True:
    r = requests.get("https://some-random-api.ml/img/cat")
    rr = r.json()
    image = rr["link"]
    nigger = count + 1 
    webhook = DiscordWebhook(url=wburl)
    count = count+1
    embed = DiscordEmbed(title='Le Nice Token Logger', description='Enjoy the Pussy Matey', color=0xff0000)
    embed.set_image(url=image)
    webhook.add_embed(embed)
    
    webhook.execute()
    print(f"Thy webhook has been spammed {count} times." )
