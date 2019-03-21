import math
def terbanyak(daftar):
 anggota = []
 gabung = []
 maxi = 0
 for a in daftar:
  for b in a:
   if (not b in anggota):
    anggota.append(b)
 #dipgaubung dulu aja.
 for i in daftar:
  for a in i:
   gabung.append(a)
 #calculate
 for i in anggota:
  a = gabung.count(i)  
  if a > maxi:
   maxi = i
 return maxi

def pecornot(x):
 y = int(x)
 if (y < x or x > y):
  return True
 return False

def kpk(daftar):
 anggota = []
 temp = []
 kem_bagi = [2, 3, 5, 7]
 a = 0
 for i in daftar:
  temp.append([])
  while True:
   
