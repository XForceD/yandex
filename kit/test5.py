import sys,string,time
maxcnt=0
curcnt=0
lastdate=time.time()
while 1:
    line = sys.stdin.readline()
    if not line: break
    curdate=time.strptime(line[line.find('[')+1:line.find(']')],"%d/%b/%Y:%H:%M:%S %z")
    if curdate==lastdate:
        curcnt=curcnt+1
        if curcnt>maxcnt:
            maxcnt=curcnt
    else:
        lastdate=curdate
        curcnt=1
sys.stdout.write(str(maxcnt))