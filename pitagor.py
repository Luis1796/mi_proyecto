n = int(input("n:"))

print("El valor de n es: %d " %n)  
print("\t", end="")


for i in range(n):
	print("%d\t" %(i+1), end="")