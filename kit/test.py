import sys,string
while 1:
    line = sys.stdin.readline()
    if not line: break
    outline=line.lower()
    comment = outline.find('#')
    if comment == -1: comment=len(outline)
    got=False
    f0=0
    while 1:
        f2 = outline.find('bar',f0,comment)
        if (f2!=-1) and (outline[f2-1] in string.whitespace) and ((f2==len(outline)-1) or (outline[f2+3] in string.whitespace) or (outline[f2+3] == '#')):
            got=True
            break
        elif (f2!=-1):
            f0=f2+1
        else:
            break
    if got:
        f0=0
        while 1:
            f1 = outline.find('bar.domain.tld',f0,comment)
            if (f1!=-1) and (outline[f1-1] in string.whitespace) and ((f1==len(outline)-12) or (outline[f1+14] in string.whitespace) or (outline[f1+14] == '#')):
                outline=outline[:f1]+"baz.donemain.tld"+outline[f1+14:]
                comment=comment+2
                f0=f1+1
            elif f1!=-1:
                f0=f1+1			
            else:
                break
        f0=0				
        while 1:
            f3 = outline.find('bar',f0,comment)
            if (f3!=-1) and (outline[f3-1] in string.whitespace) and ((f3==len(outline)-1) or (outline[f3+3] in string.whitespace) or (outline[f3+3] == '.') or (outline[f3+3] == '#')):
                outline=outline[:f3]+"baz"+outline[f3+3:]
                f0=f3+1
            elif f3!=-1:
                f0=f3+1				
            else:
                break	
        sys.stdout.write(outline)
    else:
        sys.stdout.write(line)		
    						