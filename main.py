import csv
import pandas
import collections
import numpy as np
import matplotlib.pyplot as plt
import datetime

def instal(str):
    with open(str) as f:
        reader = csv.reader(f)
        l =[row for row in reader]
    l_T=trans(l)
    l_o=l_T[4]
    l_o.pop(0)
    return l_o

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def prime(A):
    pn=[2]
    for L in range(3,A):
        chk=True
        for L2 in pn:
            if L%L2 == 0:chk=False
        if chk==True:pn.append(L)
    return pn

def trans(A):
    A_T= [list(x) for x in zip(*A)]
    return A_T




l=instal('data/130001_tokyo_covid19_patients.csv')
c = collections.Counter(l)
l_data=trans(c.most_common())[1] 
l_prime=[]
for num in l_data:
    l_prime.extend(prime_factorize(num))

c_prime = collections.Counter(l_prime)
pr=sorted(c_prime.most_common())
x=prime(pr[len(pr)-1][0])
y=[]
for i in range(len(x)):
    if x[i]!=pr[i][0]:
        pr.insert(i,[x[i],0])
    else:
        pr[i]=[pr[i][0],pr[i][1]]

data_table=trans(pr)

plt.rcParams["figure.figsize"] = [10,4.0] 
plt.rcParams["xtick.labelsize"] = 5        # 目盛りのフォントサイズ

label = np.array(data_table[0])
left=np.arange(0,len(pr),1)
height = np.array(data_table[1])
plt.bar(left,height,tick_label=label,align="center",width=0.9)
plt.xlim(-0.5,len(pr)-.5)
text='data/' + str(datetime.date.today()) + '.png'
plt.savefig(text)
plt.show()
