import sys,string
numipv4=0
numipv6=0
while 1:
    line = sys.stdin.readline()
    if not line: break
    wline = line[0:44]
    f1=wline.find(':')
    if f1>0 and f1<5:
        wline=wline[f1+1:]
#        print(wline)
        f2=wline.find(':')
        if f2>0 and f2<5:		
            wline=wline[f2+1:]
#            print(wline)
            f3=wline.find(':')
            if f3>0 and f3<5:
                wline=wline[f3+1:]
#                print(wline)
                f4=wline.find(':')
                if f4>0 and f4<5:
                    wline=wline[f4+1:]
#                    print(wline)
                    f5=wline.find(':')
                    if f5>0 and f5<5:				
                        wline=wline[f5+1:]
#                        print(wline)
                        f6=wline.find(':')
                        if f6>0 and f6<5:					
                            wline=wline[f6+1:]
#                            print(wline)
                            f7=wline.find(':')
                            if f7>0 and f7<5:						
                                numipv6=numipv6+1
sys.stdout.write(str(numipv6))