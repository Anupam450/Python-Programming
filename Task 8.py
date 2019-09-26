def mulallnum(lst):
   x=1
   for i in lst:
      x=x*i
   return x
A=list()
n=int(input("Enter the size of the List ::"))
print("Enter the Element of the List ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
print("PRODUCT OF ALL NUMBERS IN THE LIST ::>",mulallnum(A))
