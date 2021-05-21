# coding=Utf-8
print("""
############################
# coder: Cüneyt TANRISEVER #
############################""")

hedef = open('/sdcard/hh.txt', 'r').readlines()
k=""
def html_decode(s):
    global k
    k=[]
    htmlCodes = (
            ('ı', '&#x131;'),
            ('İ', '&#x130;'),
            ('Ö', '&#xD6;'),
            ('ö', '&#xF6;'),
            ('ü', '&#xFC;'),
            ('Ü', '&#xDC;'),
            ('ğ', '&#x11F;'),
            ('Ğ', '&#x11E;'),
            ('ç', '&#xE7;'),
            ('Ç', '&#xC7;'),
            ('ş', '&#x15F;'),
            ('Ş', '&#x15E;'),
            ('â', '&#xE2;'),
            ('Â', '&#xC2;')
            
            
        )
    for code in htmlCodes:
        s = s.replace(code[0], code[1])
        print s
        k.append(s)
        print k
    for kj in k[-1:]:
        print kj
        hedef = open('/sdcard/hh.html', 'a')
        hedef.write(kj)
        hedef.close()
    
    
    
    
    
    
    
    
    return s
print k
kk="""dex'dexm'&"""
for i in hedef:
    html_decode(i)
