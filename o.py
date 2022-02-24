import json

a=[]

o = json.loads(open('c:\\saga\\stosaga.json').read())
for x in (o.keys()):
	for y in list(o[x].keys()):
		try:
#		if o[x][y][2]>.04131:
			a.append([x,y,o[x][y][0],o[x][y][1],o[x][y][2]])
			print([x,y,o[x][y][2]])
		except: continue
s=''

for x in a:
	print(x)
	s = s+x[0]+','+x[1]+','+str(x[4])+'\n'

p = open('c:\\saga\\dorpro.csv','w')
p.write(s)
p.close()
