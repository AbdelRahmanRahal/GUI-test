# ----- IGNORED WORDS LIST -----
ignrdwords = ["and", "as", "but", "for", "if", "nor", "or", "so", "yet", "a", "an", "the", "as", "at", "by", "for", "in", "of", "off", "on", "per", "to", "up", "via"]
cnt = 0

# ----- USER INPUT -----
inp = input("Enter a title: ")
inplist = inp.lower().split()

# ----- FIRST AND LAST WORDS' CASES -----
# frstword = inplist[0][0].upper() + inplist[0][1:]
# lstword = inplist[len(inplist) - 1][0].upper() + inplist[len(inplist) - 1][1:]
inplist[0] = inplist[0][0].upper() + inplist[0][1:]
inplist[len(inplist) - 1] = inplist[len(inplist) - 1][0].upper() + inplist[len(inplist) - 1][1:]
# inplist.pop(0)
# inplist.pop(len(inplist) - 1)

# -----
for word in inplist:
	if (word[len(word) - 1] == ":") or (word[len(word) - 1] == "—"):
		inplist[cnt + 1] = inplist[cnt + 1][0].upper() + inplist[cnt + 1][1:]
	# elif (cnt > 0) and (cnt < (len(inplist) - 1)):
	# 	if word not in ignrdwords:
	# 		inplist[cnt] = word[0].upper() + word[1:]
	elif not ((word in ignrdwords) and (cnt > 0) and (cnt < (len(inplist) - 1))):
		inplist[cnt] = word[0].upper() + word[1:] 
	else:
		pass

	cnt += 1

print(inplist)
# print(frstword, lstword, inplist)