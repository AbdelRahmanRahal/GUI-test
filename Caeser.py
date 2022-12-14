txt = input("Enter your text: ")
num = int(input("Enter the number of shifts: "))
encr = ""

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.?! *$@&"

for i in txt:
	for q in chars:
		if i == q:

			encr = encr + chars[chars.find(i) + num]
print(encr)