import sys,string
while 1:
    line = sys.stdin.readline()
    if not line: break
    outline=line.lstrip().rstrip()
    if len(outline)>0:
        curparams=outline.split();
        if curparams[0]=='hosts:' and curparams[1]!='dns':
            for i in range(len(curparams)-1):
                if curparams[i+1]=='dns':
                    bucket2='dns'
                    for ii in range(i+1):
                        bucket=curparams[ii+1]
                        curparams[ii+1]=bucket2
                        bucket2=bucket
            outline="\t"
            outline=outline.join(curparams)+"\n"
            sys.stdout.write(outline)
        else:
            sys.stdout.write(line)
    else:
        sys.stdout.write(line)