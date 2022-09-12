#program to find first non repeating character: 

myStr = input("Enter the string : ")
while myStr != "":
	slen0 = len(myStr)
	ch = myStr[0]
	myStr = myStr.replace(ch, "")
	slen1 = len(myStr)
	if slen1 == slen0-1:
		print ("First non-repeating character = ",ch)
		break;
	else:
		print ("No Unique Character Found!")