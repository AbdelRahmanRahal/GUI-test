# ----- DECLARATIONS -----
ignrdwords = ["and", "as", "but", "for", "if", "nor", "or", "so", "yet", "a", "an", "the", "as", "at", "by", "for", "in", "of", "off", "on", "per", "to", "up", "via"]
cnt = 0

# ----- FIRST LETTER CAPITALISER -----
def FrstLttr():
	inplist[cnt] = inplist[cnt][0].upper() + inplist[cnt][1:]

# ----- USER INPUT -----
inp = input("Enter a title: ")
inplist = inp.lower().split()

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
output = " ".join(inplist)
print(output)