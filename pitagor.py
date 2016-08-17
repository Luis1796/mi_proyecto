n = int(input("n:"))

print("El valor de n es: %d " %n)  
print("\t", end="")


for i in range(n):
	print("%d\t" %(i+1), end="") 

print("")

for i in range(1, n+1):
	print("%d\t"%i, end="")
	for j in range(1,n+1): 
		print("%d\t "%(i*j), end="")