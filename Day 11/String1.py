punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''  

str = input("Enter a string: ")  
  
punct = ""  
for ch in str:  
   if ch not in punctuation:  
       punct = punct + ch  

print(punct) 
