#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#practical 1.1 caesar cipher


# In[ ]:


def encrypt(text,key,alpha): ##alpha ==>alphabet
    cipher=''
    for i in range(0,len(text)):
        if(text[i]==" "):
            cipher+=" "
        else:
            pl=text[i]
            position=alpha.index(pl)
            c=(position+key)%26 ##formula
            cipher+=alpha[c]
            print("Encryption:",cipher)
    return cipher

def decrypt(cipher,key,alpha):
    dc=''
    for i in range(0,len(cipher)):
        if(cipher[i]==" "):
            dc+=" "
        else:
            pl=cipher[i]
            position=alpha.index(pl)
            c=(position-key)%26 ##formula
            dc+=alpha[c]
            print("Decryption:",cipher)
    return dc

alpha='abcdefghijklmnopqrstuvwxyz'
text=input("enter plain text:").lower()
key=int(input("enter key of ur choice: "))
new=encrypt(text,key,alpha) ##calling the function with parameters text,key,alpha
print("the encrypted text is ",new)
old=decrypt(new,key,alpha)
print("the decrypted text is ",old)


# In[ ]:


##practical 2.1monoalphabetic cipher(multiplicative)


# In[4]:


from sympy import mod_inverse
import math

def encrypt(text,key,alpha):
    cipher=''
    for i in range(0,len(text)):
        if(text[i]==" "):
            cipher+=" "
        else:
            pl=text[i]
            position=alpha.index(pl)
            c=(position*key)%26 ##formula
            cipher+=alpha[c]
            print("Encryption:",cipher)
    return cipher

def decrypt(cipher,key,alpha):
    dc=''
    for i in range(0,len(cipher)):
        if(cipher[i]==" "):
            dc+=" "
        else:
            pl=cipher[i]
            position=alpha.index(pl)
            mi=mod_inverse(key,26)
            c=int(position*mi)%26
            print(c)
            dc+=alpha[c]
            print("decryption: ",dc)
    return dc

alpha='abcdefghijklmnopqrstuvwxyz'
text=input("enter plain text:").lower()
key=int(input("enter key of ur choice: "))

new=encrypt(text,key,alpha) ##calling the function with parameters text,key,alpha
print("the encrypted text is ",new)
old=decrypt(new,key,alpha)
print("the decrypted text is ",old)


# In[ ]:


##practical 2.2 Monoaphabetic cipher (affline)


# In[4]:


from sympy import mod_inverse
import math

def encrypt(text,k1,k2,alpha):
    cipher=''
    for i in range(0,len(text)):
        if(text[i]==" "):
            cipher+=" "
        else:
            pl=text[i]
            position=alpha.index(pl)
            c=(position*k1)%26
            c1=(c+k2)%26
            cipher+=alpha[c1]
            print("encryption:",cipher)
    return cipher

def decrypt(cipher,k1,k2,alpha):
    dc=''
    for i in range(0,len(cipher)):
        if(cipher[i]==" "):
            dc+=" "
        else:
            pl=cipher[i]
            position=alpha.index(pl)
            mi=mod_inverse(k1,26)
            c=(position-k2)%26
            c1=int(c*mi)%26
            dc+=alpha[c1]
            print("decryption:",dc )
    return dc

alpha='abcdefghijklmnopqrstuvwxyz'
text=input("enter plain text:").lower()
key1=int(input("enter first key:"))
key2=int(input("enter second key:"))

newText=encrypt(text,key1,key2,alpha)
print("the encrypted text is:",newText)

oldText=decrypt(newText,key1,key2,alpha)
print("the decrypted text is:",oldText)


# In[ ]:


##practical 3.1 RailFenceCipher


# In[10]:


text=input("enter plain text: ")
row=int(input("enter level of depth: "))
col=len(text)
mat=[]
ivalue=[]
count=0
cipher=""
for i in range(0,row):
    mat1=[]
    for j in range(0,col):
        mat1.append([' '])
    mat.append(mat1)
    
while count<col:
    for j in range(0,row-1):
        count+=1
        ivalue.append(j)
    for j in range(row-1,0,-1):
        count+=1
        ivalue.append(j)

for i in range(0,col):
    mat[ivalue[i]][i]=text[i]
    
for i in range(0,row):
    print(mat[i])
    
for i in range(0,row):
    for j in range(0,col):
        if mat[i][j]!=[' ']:
            cipher+=mat[i][j]
    cipher+='|'
print()
print("encrypted text: ",cipher)


# In[6]:


##practical 4 RSA Algorithm


# In[12]:


import math
def gcd(x,y):
    temp=0
    while(1):
        temp=x%y
        if (temp==0):
            return y
        x=y 
        y=temp

p1=int(input("enter first prime number: "))
p2=int(input("enter second prime number: "))
pk=p1*p2

phi=(p1-1)*(p2-1)
pos=0
e=0

while(e<phi):
    if(gcd(e,phi)==1):
        break
    else:
        e=e+1
k=2
d=(1+(k*phi))/e

text=input("enter plain text: ")
alpha='abcdefghijklmnopqrstuvwxyz'
for i in range(0,len(text)):
    pl=text[i]
    pos+=alpha.index(pl)
cipher=(pos**e)%pk
print("cipher value: ",cipher)

decrypt=(cipher**d)%pk
print("decrypted value: ",decrypt)


# In[ ]:


##practical 5.1 deffiehelman


# In[13]:


import math
Xa=int(input("enter the value of Xa: "))
Xb=int(input("enter the value of Xb: "))

p=int(input("enter a prime number: "))
a=int(input("enter primitive root with condition that a<p: "))

Ya=((math.pow(a,Xa))%p);
Yb=((math.pow(a,Xb))%p);
Ka=((math.pow(Yb,Xa))%p);
Kb=((math.pow(Ya,Xb))%p);

if(Ka==Kb):
    print("Transmission successful");
else:
    print("Transmission failed");


# In[ ]:



##practical 5.2 deffie helman


# In[3]:


import math

p=int(input("enter modulo"))
g=int(input(f"enter primitive root of {p}:"))
a=int(input("choose 1st secret no for alice:"))
b=int(input("choose 2nd secret no for bob:"))

A=math.pow(g,a)%p;
B=math.pow(g,b)%p;

S_A=math.pow(B,a)%p;
S_B=math.pow(A,b)%p;

if(S_A==S_B):
    print("Alice and Bob can communicate with each other,,noice");
    print("they share a secret number==>",S_A);
else:
    print("Alice and Bob cant communicate with each other,,sad");


# In[ ]:


##practical 6 MD5 algorithm


# In[6]:


import hashlib

text="me mare hue jeetu ka langotiya yaar"
output=hashlib.md5(text.encode())
print("hash of the input string: ")
print(output.hexdigest())


# In[ ]:


##practical 7 HMAC-SHA256 SIgnature


# In[8]:


import hmac
import hashlib

secret_key=b"NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
total_params=b"/public/api/ver1/accounts/new?type=binance&name=binance_account&api_key=XXXXXX&secret=YYYYYY"

signature=hmac.new(secret_key,total_params,hashlib.sha256).hexdigest()
print("signature={0}".format(signature))

