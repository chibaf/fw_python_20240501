import os
import datetime

f=open("teste.txt",'a',encoding="utf-8")

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
d = now.strftime('%Y %m %d %H:%M:%S')
s1=d+" teste starts\n"
os.system('echo "test01">> teste.txt')
os.system('echo "test02">> teste.txt')
f.write(s1)
f.close()
os.system('echo "test03">> teste.txt')
exit()
