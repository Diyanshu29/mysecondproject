print("Prime Number...")
no=int(input("Enter Number to Check for Prime:"))

for i in range(2,no):
	if(no%i==0):
		print("Given number "+str(no)+", is Not a Prime Number..")
		break
else:
	print("Given number "+str(no)+", is a Prime Number..")
