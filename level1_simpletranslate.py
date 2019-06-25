#Level 1 for the Python Challenge

#Defining a function for our simple translation
def simpletranslate(string):
	#Creating a list of alphabets
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	#Then creating a list of numeric values with list comprehension
	value = [i for i in range(1,27)]

	#Creating a tuple matching a numeric value to each alphabet with zip, before making it a dictionary
	pair = zip(alphabet, value)
	pair = dict(pair)

	#Then creating a tuple reverse matching an alphabet to each numeric value, before making it a dictionary
	antipair = zip(value, alphabet)
	antipair = dict(antipair)
	
	#Creating an empty list called 'newsentence'
	newsentence = []
	
	for letter in string:
		#Managing exceptions if the character is not an alphabetical letter. Hopefully we will get better at dealing with such regex with more practice
		if letter == " ":
			print("not a letter")
		elif letter ==".":
			print("not a letter")
		elif letter =="(":
			print("not a letter")
		elif letter ==")":
			print("not a letter")
		elif letter =="'":
			print("not a letter")
		else:
			#First, use the 'letter' variable to obtain the respective numeric value in 'pair' and save it in 'number'
			number = pair[letter]

			#Then, add 2 to 'number' (to translate the letter by two placings) and save it to 'newnumber'
			newnumber = number + 2

			#Restarting the count from 1 if 'number' is >24 or if 'newnumber' > 26
			if newnumber >26:
				newnumber = newnumber - 26
				newletter = antipair[newnumber]
				newsentence.append(newletter)

			#If not, we use the 'newnumber' variable to obtain the respective alphabet in 'antipair' and save it in 'newletter'
			else:
				newletter = antipair[newnumber]
				newsentence.append(newletter)

	#Combine all the new character elements in our 'newsentence' list for better readability
	print(''.join(newsentence))

simpletranslate("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
simpletranslate("map")