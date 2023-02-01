import json

s=[]
s2=[]
a = json.loads(open('c:\\saga\\fullcorp.json').read())
for x in a:
	for y in list(x.keys()):
		try:
#	continue
			n = []
			d = []
			z = x[y]
			print(z)
			ssd = y.upper()
			d.append(y)
			d.append(z[1][y]['annualHoldingsTurnover'])
			d.append(z[1][y]['enterpriseToRevenue'])
			d.append(z[1][y]['beta3Year'])
			print(d)
			d.append(z[1][y]['profitMargins'])
			d.append(z[1][y]['enterpriseToEbitda'])
			d.append(z[1][y]['52WeekChange'])
			d.append(z[1][y]['morningStarRiskRating'])
			d.append(z[1][y]['forwardEps'])
			d.append(z[1][y]['revenueQuarterlyGrowth'])
			d.append(z[1][y]['sharesOutstanding'])
			d.append(z[1][y]['fundInceptionDate'])
			d.append(z[1][y]['annualReportExpenseRatio'])
			d.append(z[1][y]['totalAssets'])
			d.append(z[1][y]['bookValue'])
			d.append(z[1][y]['sharesShort'])
			d.append(z[1][y]['sharesPercentSharesOut'])
			d.append(z[1][y]['fundFamily'])
			d.append(z[1][y]['lastFiscalYearEnd'])
			d.append(z[1][y]['heldPercentInstitutions'])
			d.append(z[1][y]['netIncomeToCommon'])
			d.append(z[1][y]['trailingEps'])
			d.append(z[1][y]['lastDividendValue'])
			d.append(z[1][y]['SandP52WeekChange'])
			d.append(z[1][y]['priceToBook'])
			d.append(z[1][y]['heldPercentInsiders'])
			d.append(z[1][y]['nextFiscalYearEnd'])
			d.append(z[1][y]['yield'])
			d.append(z[1][y]['mostRecentQuarter'])
			d.append(z[1][y]['shortRatio'])
			d.append(z[1][y]['sharesShortPreviousMonthDate'])
			d.append(z[1][y]['floatShares'])
			d.append(z[1][y]['beta'])
			d.append(z[1][y]['enterpriseValue'])
			d.append(z[1][y]['priceHint'])
			d.append(z[1][y]['threeYearAverageReturn'])
			d.append(z[1][y]['lastSplitDate'])
			d.append(z[1][y]['lastSplitFactor'])
			d.append(z[1][y]['legalType'])
			d.append(z[1][y]['morningStarOverallRating'])
			d.append(z[1][y]['earningsQuarterlyGrowth'])
			d.append(z[1][y]['priceToSalesTrailing12Months'])
			d.append(z[1][y]['dateShortInterest'])
			d.append(z[1][y]['pegRatio'])
			d.append(z[1][y]['ytdReturn'])
			d.append(z[1][y]['forwardPE'])
			d.append(z[1][y]['maxAge'])
			d.append(z[1][y]['lastCapGain'])
			d.append(z[1][y]['shortPercentOfFloat'])
			d.append(z[1][y]['sharesShortPriorMonth'])
			d.append(z[1][y]['impliedSharesOutstanding'])
			d.append(z[1][y]['category'])
			d.append(z[1][y]['fiveYearAverageReturn'])
			n.append(y)
		
			n.append(z[0][y]['ebitdaMargins'])	
			n.append(z[0][y]['profitMargins'])
			n.append(z[0][y]['grossMargins'])
			n.append(z[0][y]['operatingCashflow'])
			n.append(z[0][y]['revenueGrowth'])
			n.append(z[0][y]['operatingMargins'])
			n.append(z[0][y]['ebitda'])
			n.append(z[0][y]['targetLowPrice'])
			n.append(z[0][y]['recommendationKey'])
			n.append(z[0][y]['grossProfits'])
			n.append(z[0][y]['freeCashflow'])
			n.append(z[0][y]['targetMedianPrice'])
			n.append(z[0][y]['currentPrice'])
			n.append(z[0][y]['earningsGrowth'])
			n.append(z[0][y]['currentRatio'])
			n.append(z[0][y]['returnOnAssets'])
			n.append(z[0][y]['numberOfAnalystOpinions'])
			n.append(z[0][y]['targetMeanPrice'])
			n.append(z[0][y]['debtToEquity'])
			n.append(z[0][y]['returnOnEquity'])
			n.append(z[0][y]['targetHighPrice'])
			n.append(z[0][y]['totalCash'])
			n.append(z[0][y]['totalDebt'])
			n.append(z[0][y]['totalRevenue'])
			n.append(z[0][y]['totalCashPerShare'])
			n.append(z[0][y]['financialCurrency'])
			n.append(z[0][y]['maxAge'])
			n.append(z[0][y]['revenuePerShare'])
			n.append(z[0][y]['quickRatio'])
			n.append(z[0][y]['recommendationMean'])
#			print(n)
#			print(d)
			s.append(d)
			s2.append(n)
		except: continue
a = ''
b=''
print(s)
print(s2)
for x in range(len(s)):
	for y in s[x]:
		a = a+str(y)+','
	a=a+'\n'

for x in range(len(s2)):
	for y in s2[x]:
		b = b+str(y)+','
	b=b+'\n'

f = open('c:\\saga\\fullcorpdata.csv','w')
f.write(a)
f.close()

f = open('c:\\saga\\fullcorpstats.csv','w')
f.write(b)
f.close()