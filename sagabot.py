import discord,asyncio,os
from discord.ext import commands, tasks
from yahoofinancials import YahooFinancials
import json
from discord import Intents
from neuralintents import GenericAssistant
import requests

def opencountry():
	a=open('c:\\saga\\corporation.csv').read().split('\n')
	b=[]
	for x in a:
		c=x.split(',')
		b.append(c)
	return b	

def countryandindustry(c,i):
	o = []
	for x in b:
		if x[4]==c and x[3]==i:
			o.append(x)
	return o

def industrybycountry(i,c):
	o = []
	for x in b:
		if x[4]==c: o.append(x)
	return o

def countrybyindustry(c,i):
	o=[]
	for x in b:
		if x[3]==i: o.append(x)
	return o


b=opencountry()

#cb = GenericAssistant("c:\\saga\\arch\\intents.json")
#cb.train_model()
#cb.save_model()

client = discord.Client()
f=open("c:\\saga\\arch\\intents.json", "r")
#ins = Intents()
#json.load(f)
#client = commands.Bot(command_prefix="!", intents=ins)

@client.event
async def on_ready():  #  Called when internal cache is loaded
	print('{0.user}'.format(client))

@client.event
async def on_message(message):
	username = str(message.author).split('#')[0]
	userm = str(message.content)
	channel = str(message.channel.name)
	print(f'{username}: {userm} ({channel})')
	
	if message.author == client.user:
		return

	if message.content.startswith('$sagadog'):
		await message.channel.send(f'Hello {username}!')
		r = userm[9:]
		print(r)
		yf = YahooFinancials(r)
		ng=''
		b=''
		h=''
		try:
			url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+r+'&apikey=0L0J5NK5GLIQR3LG'
			r = requests.get(url)
			data = r.json()
			rf = data['Name']
			rg = data['Description']
			sector = data['Sector']
			industry = data['Industry']
			mcap = data['MarketCapitalization']
		except:
			pass
		try:
			b = yf.get_summary_data(True)
			g=list(b.keys())
			for x in list(b[g[0]].keys()):
				h=h+str(x)+'\t'+str(b[g[0]][x])+'\n'		
			
		except: pass

		await message.channel.send(f'{g[0]}')
		await message.channel.send(f'{h}')
		await message.channel.send(f'{ng}') 

client.run("OTc3MTc1MzkyMzYyMzAzNDk4.GndIP_.W4aiRn74SADJKu3nGdyOEVadC_vtiu2nfaj4wQ")  # Starts up the bot
