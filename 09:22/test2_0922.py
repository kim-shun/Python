import re
prog = re.compile('(K|S)u(r|s)(a|o)nf?(a|o)(o|m)?g?i?(saya)?', re.IGNORECASE)
ret = prog.search('KUSANAGISAYA')
ret2 = prog.search('Kuronami')
ret3 = prog.search('SUSANOO')
ret4 = prog.search('kusanomi')
#ret5 = prog.search('SuZunone') #エラー
print(ret[0])
print(ret2[0])
print(ret3[0])
print(ret4[0])
#print(ret5[0])
