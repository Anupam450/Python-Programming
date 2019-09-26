A=list()
even=odd=0
n=int(input("Enter the size of the List ::"))
print("Enter the Element of the List ::")
for i in range(int(n)):
    k=int(input(""))
    A.append(k)
    if(k%2==0):
       even=even+1
    else:
        odd=odd+1
