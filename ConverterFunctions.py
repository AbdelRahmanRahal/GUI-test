# ----- TITLE CASE -----
def Title(txt):
	# ----- DECLARATIONS -----
	ignrdwords = ["and", "as", "but", "for", "if", "nor", "or", "so", "yet", "a", "an", "the", "as", "at", "by", "for", "in", "of", "off", "on", "per", "to", "up", "via"]
	cnt = 0

	# ----- FIRST LETTER CAPITALISER -----
	def FrstLttr():
		inplist[cnt] = inplist[cnt][0].upper() + inplist[cnt][1:]

	# ----- USER INPUT -----
	inplist = txt.lower().split()

	# ----- TITLE CASE CONVERTER -----
	for word in inplist:
		if (cnt == 0) or (cnt == (len(inplist) - 1)):
			FrstLttr()
		elif inplist[cnt - 1][len(inplist[cnt - 1]) - 1] in ":—":
			FrstLttr()
		elif word not in ignrdwords:
			FrstLttr()
		cnt += 1

	# ----- OUTPUT -----
	titled = " ".join(inplist)
	return titled

# ----- ALT CASE -----
def Alt(txt):
	alted = ""

	for char in range(len(txt)):
		if char % 2:
			alted += txt[char].lower()
		else:
			alted += txt[char].upper()

	return alted

# ----- CAESAR CIPHER -----
def Caesar(txt, shift):
	encrypted = ""

	for char in txt:
		encrypted += chr(ord(char) + shift)

	return encrypted