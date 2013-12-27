import sys,string
numstr=0
wloss=0.0
wstdev=0.0
wavg=0.0
while 1:
    line = sys.stdin.readline()
    if not line: break
    f=line.find('.')
    if f!=-1:
        curstr=int(line[0:f])
        curparams=line.split();
        curstr=int(line[0:f])
        curloss=float(curparams[2][:len(curparams[2])-1])
        curstdev=float(curparams[8])
        curavg=float(curparams[5])
        if curloss==wloss:
            if curstdev==wstdev:
                if curavg>wavg:
                    numstr=curstr
                    wloss=curloss
                    wstdev=curstdev
                    wavg=curavg
            elif curstdev>wstdev:
                numstr=curstr
                wloss=curloss
                wstdev=curstdev
                wavg=curavg	
        elif curloss>wloss:
            numstr=curstr
            wloss=curloss
            wstdev=curstdev
            wavg=curavg
if numstr!=0:
    sys.stdout.write(str(numstr))