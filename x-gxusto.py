#! python3
#perfektigo.py- gxustigi tekstajxojn en gxustajn literojn de esperanto

import sys,re,pyperclip

#teksto por la originala tekstajxo

#if len(sys.argv)>1:
#    teksto=' '.join(sys.argv[1:]) 
#else:
#    teksto=str(pyperclip.paste())


#anstatauxigi la x-sistemstilajn kombinajxojn
#malbona stilo sed klara logiko, hehehe
for i in range(6):
    teskto=re.sub('gx','ĝ',teksto)
    teskto=re.sub('Gx','Ĝ',teksto)
    teksto=re.sub('cx','ĉ',teksto)
    teksto=re.sub('Cx','Ĉ',teksto)
    teksto=re.sub('hx','ĥ',teksto)
    teksto=re.sub('Hx','Ĥ',teksto)
    teksto=re.sub('jx','ĵ',teksto)
    teksto=re.sub('Jx','Ĵ',teksto)
    teksto=re.sub('sx','ŝ',teksto)
    teksto=re.sub('Sx','Ŝ',teksto)
    teksto=re.sub('ux','ŭ',teksto)
    teksto=re.sub('Ux','ŭ',teksto)
print(teksto)
pyperclip.copy()

