#program to reverse a array

def reverse(alist):

   #intializing pointers
   left = 0
   right = len(alist)-1

   #condition for termination
   while left<right:

       #swapping
       temp = alist[left]
       alist[left] = alist[right]
       alist[right] = temp

       #updating pointers
       left += 1
       right -= 1

   return alist

size=int(input("enter size of the list: "))
lst=[]
lst1=[]
for i in range(size):
  num=int(input("Enter list value: "))
  lst.append(num)
print("The original array", lst)
reverse(lst)
print("The reversed array in place",lst)
