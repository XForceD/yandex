import sys,string
maxcnt=0
curcnt=0
lastdate=''
while 1:
    line = sys.stdin.readline()
    if not line: break
    curdate=line[1:27]
    if curdate==lastdate:
        curcnt=curcnt+1
        if curcnt>maxcnt:
            maxcnt=curcnt
    else:
        lastdate=curdate
        curcnt=1
sys.stdout.write(str(maxcnt))