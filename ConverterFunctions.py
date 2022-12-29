# ----- Title Case -----
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
	return " ".join(inplist)

# ----- AlT CaSe -----
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

# ----- Password Generator -----
def PasswordGen(txt, PGchckboxVar):
	from random import choice, randint, shuffle

	# ----- ALLOW SPACES CHECKBOX CONFIGURATION AND DECLARATIONS-----
	if PGchckboxVar.get() == False:
		symbols = "*&!$%@_"
		inplist = list(txt.replace(" ", ""))
	else:
		symbols = "*&!$%@_ "
		inplist = list(txt)

	# ----- PASSWORD GENERATOR MECHANISM -----
	for i in range(len(inplist)):
		uindex = randint(0, len(inplist)- 1)
		lindex = randint(0, len(inplist)- 1)
		inplist[uindex] = inplist[uindex].upper()
		inplist[lindex] = inplist[lindex].lower()
		inplist.append(choice(symbols))
		inplist.append(str(randint(0,9)))

	shuffle(inplist)
	return "".join(inplist)