#35.
#次の正規表現を用いたコードの【A】の部分に入れたときエラーとなるものはどれか。

import re
prog = re.compile('(K|S)us(a|u)n(a|o)(o|m)?g?i?(saya)?',re.IGNORECASE)
#【A】
ret = prog.search('SUSANOO')
ret2 = prog.search('Kus')
ret3 = prog.search('Kusaunaoooomgisaya')
ret4 = prog.search('KUSAUNAOOOMGISAYA')
ret5 = prog.search('Ke')
ret6 = prog.search('Kusaneiro')
ret7 = prog.search('Kuanaogis')
ret8 = prog.search('Kusanamgisaya')
ret9 = prog.search('KUSANAMGISAYA')
ret10 = prog.search('KusanamgisAY')
ret11 = prog.search('KusANO')
ret12 = prog.search('KusAN')

print(ret[0])
#print(ret2[0])
#print(ret3[0])
#print(ret4[0])
#print(ret5[0])
#print(ret6[0])

print(ret8[0])
print(ret9[0])
print(ret10[0])
print(ret11[0])
print(ret12[0])

#SUSANOO
#Kusanamgisaya
#KUSANAMGISAYA
#Kusanamgi


#正答: ret = prog.search('Kusaneiro')

