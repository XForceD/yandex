import sys,string
flagos=0
firstboot=0
while 1:
    line = sys.stdin.readline()
    if not line: break
    fb=line.find('<os>')
    fe=line.find('</os>')
    if fb!=-1:
        flagos=1
    if fe!=-1:
        if firstboot==0:
            line=line[0:fe]+"<boot dev='hd' />\n"+line[fe:]		
        flagos=0
    if flagos==1:
        if line.find('<kernel>')!=-1:
            ffb=line.find('<kernel>')
            ffe=line.find('</kernel>')
            line=line[0:ffb]+line[ffe+9:]
        if line.find('<initrd>')!=-1:
            ffb=line.find('<initrd>')
            ffe=line.find('</initrd>')
            line=line[0:ffb]+line[ffe+9:]
        if line.find('<loader>')!=-1:
            ffb=line.find('<loader>')
            ffe=line.find('</loader>')
            line=line[0:ffb]+line[ffe+9:]
        if line.find('<cmdline>')!=-1:
            ffb=line.find('<cmdline>')
            ffe=line.find('</cmdline>')
            line=line[0:ffb]+line[ffe+10:]			
        if line.find('<bootmenu')!=-1:	
            ffb=line.find('<bootmenu')
            ffe=line.find('/>',ffb)
            line=line[0:ffb]+line[ffe+2:]
        if line.find('<bootloader>')!=-1:
            ffb=line.find('<bootloader>')
            ffe=line.find('</bootloader>')
            line=line[0:ffb]+line[ffe+13:]		
        if line.find('<boot')!=-1:	
            ffb=line.find('<boot')
            ffe=line.find('/>',ffb)
            if firstboot==0:
                 line=line[0:ffb]+"<boot dev='hd' />"+line[ffe+2:]
            else:
                 line=line[0:ffb]+line[ffe+2:]			
            firstboot=1
        if len(line.rstrip().lstrip())!=0:		
            sys.stdout.write(line)			
    else:
        sys.stdout.write(line)	