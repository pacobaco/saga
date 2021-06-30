from yahoofinancials import YahooFinancials

def divy(x,y):
	return x/y

def rund(e):
	w={}
	for x in e:
		if x:
			r=divy(float(x[1]),float(x[2]))
			if r in w:
				w[r].append(x[0])
				w[r].append(x[3])
			else:
				w[r]=[]
				w[r].append(x[0])
				w[r].append(x[3])
	return w

o = open('c:\\saga\\saga')
r = o.read()
r=r.replace('"','')
print(r)
e=r.split('\n')

#i=open('n2dog')
#kl=i.read()
#pok=kl.split('\n')
#il=len(pok)
#print kl
#uo=kl
#i.close()

sto = []

for x in e[0:6493]:
	print(x)
#       i=open('scf','w')
#       uo=i.read()
#       try:
        #x='AAPL'
#       try:
	print(x)
	yf=YahooFinancials(x)
#       except:
#               print 'err'
#               continue
	m=yf.get_financial_stmts('quarter','balance')
	print(m)
	z=list(m.keys())
	print(z)
	w=z[0]
	r=m[w]
	u=list(r.keys())
	print(u)
	f=r[u[0]] 
	try:
		h=f[0]
	except:
		continue
	j=list(h.keys())
	dt=j
	k=h[j[0]]
	try:
		l=k['totalAssets']
		c=yf.get_ebit()
	except:
		continue
#	uo=uo+x+','+str(c)+','+str(l)+'\n'
        #bb=bb+uo
#       i.write(bb)
#       i.close()
	s = []
	s.append(x)
	s.append(c)
	s.append(l)
	s.append(dt)
	sto.append(s)
	print(x,c,l,'\n')
#       except:
#       continue
print(sto)  
print(rund(sto))
h=rund(sto)
b=list(h.keys())
b.sort()
for x in b:
	print(x,h[x][0],h[x][1])
print(len(b))
#o=open('nasdog','w')
#o.write(uo)
#o.close()

