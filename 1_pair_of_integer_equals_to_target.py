#finding the pair of integers that equals to target value :

size=int(input("enter size of the list: "))
lst=[]
lst1=[]
for i in range(size):
  num=int(input("Enter list value: "))
  lst.append(num)
target=int(input("Enter target value: "))
for i in lst:
  for j in lst :
    if i == j :
      continue
    else:
      sum=i+j
      if i and j not in lst1:
        if target==sum:
          print(f"The Two numbers that needed to be added to get {target} is {i} and {j}")
          lst1.append(i)
          lst1.append(j)
        else:
          continue
      else:
        continue