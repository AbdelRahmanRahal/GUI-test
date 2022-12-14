def Caesar(txt):
	shift = 3
	encrypted = ""

	for char in txt:
		encrypted += chr(ord(char) + shift)

	return encrypted