n=int(input("enter the value of n"))
sum=0


while(n>0):
	rem=n%10
	sum=sum+rem
	n//=10
print("the sum of the digits of given number is",sum)
	
