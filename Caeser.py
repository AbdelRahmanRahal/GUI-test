txt = input("Enter a text: ")
num = int(input("Enter the number of shifts: "))
encr = ""

for i in txt:
	encr += chr(ord(i) + num)

print(encr)

