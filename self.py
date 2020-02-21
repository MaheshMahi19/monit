import discord
from discord import Webhook,RequestsWebhookAdapter
import aiohttp
client = discord.Client()

@client.event
async def on_ready():
    print("Self bot is ready...!",client.user.id)


@client.event
async def on_message(message):
    #cl = [545791218743902220] #channels ID's #general
    #cs = client.get_channel(560423218184192021) #channel id to send messages for to be copied by bot #test

    #md = {"680321947166572554":"https://discordapp.com/api/webhooks/680357110269476869/P2UuUtbRa6ufx2m8q8Lg48Arx5aCVqSVlDmS26jY08tgCJnkLlqewyTm21QHpJE5oLFw","680321976539283566":"https://discordapp.com/api/webhooks/680357508992598026/2tfriUvjG5juqm-yL9bZeJ3y5WdPHejdCyGS5FiscIuEbBelc38Cy78k9jMxeSH0iRkc"}
    if str(message.channel.id) in md:
        wbId,wbTok = md[str(message.channel.id)].split("/")[-2],md[str(message.channel.id)].split("/")[-1]
        wb = Webhook.partial(int(wbId),wbTok,adapter=RequestsWebhookAdapter())
        if len(message.embeds) != 0:
            wb.send(embeds=message.embeds)
        if len(message.attachments) != 0:
            for at in message.attachments:
                fi = await at.to_file()
                wb.send(file=fi)
        if message.content != "" or message.content != " ":
            try:
                wb.send(message.content)
            except Exception as e:
                print(message.content)
client.run("mfa.vI_ndYBVOI28xT2wDwhrX7U5ITXD5GeuJtzIF11O7B78Km9Sw3es07ByAqOlWnx4tZ8qHhqToFATp21t8185",bot=False)
