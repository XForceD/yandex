import sys,string,tarfile
#import os
tar = tarfile.open("etc.tar.gz", "r:gz")
skip = 0
inittabres = "5"
useinittab = 0
res="5"
existinittab = 0
for files in tar.getmembers():
#    print(files.name)
#    print(os.path.splitext(files.name))
    if files.name == 'etc/init/rc-sysinit.conf':
        #print('BINGO!')	
        fil=tar.extractfile(files)
        while 1:
            line = fil.readline().decode("utf-8")
            #print(line)
            if not line: break
            skip=0
            for i in range(len(line)):
                if line[i] not in string.whitespace:
                    if line[i]=='#':
                        skip=1
                        break
                    else:
                        break
            if skip==0:
                fbb=line.find('/etc/inittab')
                if fbb!=-1:
                    useinittab = 1
                fb=line.find('env DEFAULT_RUNLEVEL')
                #print(str(fb))
                if fb!=-1:
                    res=line[fb+16:]
                    for i in range(len(res)):	
                        if res[i] in string.digits:
                            res=res[i]
                            break
                    if len(res)!=1:
                        res="5"				
    elif files.name == 'etc/inittab':
        #print('BINGO!')	
        existinittab = 1
        fil=tar.extractfile(files)
        while 1:
            line = fil.readline().decode("utf-8")
            #print(line)
            if not line: break
            fb=line.find(':initdefault:')
            #print(str(fb))
            if fb!=-1:
                inittabres=line[fb-1]
if useinittab==1 and existinittab==1:
    res=inittabres			
tar.close()
sys.stdout.write(res)