
                    
strIn = input (“Enter a string :”)

words = [word.lower () for word in strIn.split ()]

words.sort ()

print("Ascending order of given string is - ")
for word in words:
    print (word)
