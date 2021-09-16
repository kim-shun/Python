from datetime import date
now = date.today()
print(now)
ns = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(ns) #09-16-21. 16 Sep 2021 is a Thursday on the 16 day of September.
birthday = date(1999,2,5)
age = now - birthday
print(age.days)

import zlib
s =  b'witch which has which witches wrist watch'
print(len(s)) #41
t = zlib.compress(s)
print(len(t)) #37
zlib.decompress(t)
print(zlib.crc32(s)) #226805979

#時間計測
from timeit import Timer
t1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
t2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(t1) #0.016031691000000015
print(t2) #0.015808191000000027

import reprlib
r = reprlib.repr(set('supercalifragilisticexpialidocious'))
print(r) #{'a', 'c', 'd', 'e', 'f', 'g', ...}

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
pprint.pprint(t, width=30)
'''
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
'''

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))
'''
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
'''

dd = '''
AA
AA
'''
print(len(dd)) #7

v = '3.14'
print(v.zfill(7)) #0003.14
