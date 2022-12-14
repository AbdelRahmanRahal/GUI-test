# ----- Alt Case -----
def Alt(txt):
	alted = ""

	for char in range(len(txt)):
		if char % 2:
			alted += txt[char].lower()
		else:
			alted += txt[char].upper()

	return alted

# ----- Caesar Cipher -----
def Caesar(txt, shift):
	encrypted = ""

	for char in txt:
		encrypted += chr(ord(char) + shift)

	return encrypted