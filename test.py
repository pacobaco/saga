from yahoofinancials import YahooFinancials
import json

u = open('c:\\saga\\bric.txt')
u = u.read().split('\n')
stocklist = ['aapl', 'mo', 'msft']
stocklist=u
symdic={}
for x in stocklist:
	try:
		print(x)
		a = YahooFinancials(x)
		b = a.get_financial_stmts('quarterly', 'income')
		b2 = a.get_financial_stmts('quarterly', 'balance')
		incq = b['incomeStatementHistoryQuarterly'][x.upper()]
		balq = b2['balanceSheetHistoryQuarterly'][x.upper()]
		datedic={}
#	try:
		for y in incq:
			listinc = list(y.keys())
			for z in listinc:
				datedic[z]=[]
				datedic[z].append(y[z]['ebit'])
			
				print(z,y[z]['ebit'])
		for y2 in balq:
			dd = list(y2.keys())
			for z2 in dd:
				datedic[z2].append(y2[z2]['totalAssets'])
				datedic[z2].append(float(datedic[z2][0])/float(y2[z2]['totalAssets']))
				print(z2,y2[z2]['totalAssets'],float(datedic[z2][0])/float(y2[z2]['totalAssets']))
		symdic[x]=datedic

	except:
		continue

with open('c:\\saga\\stobric.json', 'w') as fp:
    json.dump(symdic, fp,indent=4)
