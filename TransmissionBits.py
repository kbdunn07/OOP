A = [-1, -1, -1, 1, 1, -1, 1, 1]
B = [-1, -1, 1, -1, 1, 1, 1, -1]
C = [-1, 1, -1, 1, 1, 1 -1, -1]
D = [-1, 1, 1, 1, -1, -1, 1, -1]
E = [1, -1, 1, -1, -1, 1, 1,-1]

S1 = B.copy()


S2 = A.copy()
i = 0;
for x in B:
  S2[i] += x
  i+=1

S3 = S2.copy()
i=0
for x in C:
  S3[i] -= x
  i+=1
i=0
for x in D:
  S3[i] += x
  i+=1


S4 = A.copy()
i=0
for x in B:
  S4[i] -= x
  i+=1
i=0
for x in C:
  S4[i] += x
  i+=1

S5 = A.copy()
i=0
for x in C:
  S5[i] += x
  i+=1
i=0
for x in D:
  S5[i] += x
  i+=1

S6 = S2.copy()
i=0
for x in C:
  S6[i] += x
  i+=1
i=0
for x in D:
  S6[i] -= x
  i+=1

S7 = A.copy()
i=0
for x in B:
  S7[i] -= x
  i+=1
i=0
for x in D:
  S7[i] += x
  i+=1
i=0
for x in E:
  S7[i] += x
  i+=1

def TransmissionBits(channel):
  i=0
  tS1=S1.copy()
  tS2=S2.copy()
  tS3=S3.copy()
  tS4=S4.copy()
  tS5=S5.copy()
  tS6=S6.copy()
  tS7=S7.copy()
  for x in channel:
    tS1[i]*=x
    tS2[i]*=x
    tS3[i]*=x
    tS4[i]*=x
    tS5[i]*=x
    tS6[i]*=x
    tS7[i]*=x
    i+=1
  
  print(f"{tS1}/8 = {(int) (sum(tS1) / 8)}")
  print(f"{tS2}/8 = {(int) (sum(tS2) / 8)}")
  print(f"{tS3}/8 = {(int) (sum(tS3) / 8)}")
  print(f"{tS4}/8 = {(int) (sum(tS4) / 8)}")
  print(f"{tS5}/8 = {(int) (sum(tS5) / 8)}")
  print(f"{tS6}/8 = {(int) (sum(tS6) / 8)}")
  print(f"{tS7}/8 = {(int) (sum(tS7) / 8)}")
  
TransmissionBits(D)
    
    

