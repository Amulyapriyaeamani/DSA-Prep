n=input("Enter a number: ")
length=len(n)
sum=0
for i in n:
    sum+=(int(i)**length)

if int(n)==sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
