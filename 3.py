
while True:
	n = int(input("Enter the number"))
	rev = 0
	if n != 00000:
		while n > 0:
			a = n % 10
			rev = rev * 10 + a
			n = n // 10

		print(rev)
	else:
		break

