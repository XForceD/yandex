import sys,string,tarfile
tar = tarfile.open("input.tgz", "r:gz")
maxusage = 0
namemax = 'null'
cntslash = 0
for files in tar.getmembers():
    fn=files.name.find('cpuacct.usage')
    if fn==len(files.name)-13:
        fil=tar.extractfile(files)
        while 1:
            line = fil.readline().decode("utf-8")
            if not line: break
            if (((int(line)>maxusage) and (files.name.count('/')==cntslash)) or (files.name.count('/')>cntslash)) :
                maxusage=int(line)
                cntslash=files.name.count('/')
                fb=files.name[:fn-1].rfind('/')
                namemax=files.name[fb+1:fn-1]				
tar.close()
sys.stdout.write(namemax)