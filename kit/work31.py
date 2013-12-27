import sys,string
numipv4=0
numipv6=0
while 1:
    line = sys.stdin.readline()
    if not line: break
    parline=line.split();
    #print(parline)
    wline = parline[0]
    #print(wline)
    #f1=wline.find(':')
    if wline.count(':')==7 or (wline.count('::')==1 and wline.count(':')>2 and wline.count(':')<8):
        numipv6=numipv6+1				
sys.stdout.write(str(numipv6))