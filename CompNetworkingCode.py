generator = ["x5", "x2", "1"]
degrees = []
for i in generator:
    degrees.append(i.replace("x", ""))
max_degree = int(max(degrees))
completeDegrees = []
for i in range(1, max_degree+1):
    completeDegrees.append(i)
completeDegrees.sort()
completeDegrees.reverse()
for i in completeDegrees:
  i=str(i)
print(completeDegrees)
j=0
for i in completeDegrees:
  if i in degrees:
    completeDegrees[j].replace(i, "0")
  j+=1
print(completeDegrees)
print(degrees)
