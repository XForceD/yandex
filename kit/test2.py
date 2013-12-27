import sys,string
count=0
while 1:
    line = sys.stdin.readline()
    if not line: break
    f1=line.find(':')
#    user=line[0:f1]
    f2=line.find(':',f1+1)
    passw=line[f1:f2]
    z1=passw.find('*')
    z2=passw.find('!')
    if z1==-1 and z2==-1:
        count=count+1
sys.stdout.write(str(count))