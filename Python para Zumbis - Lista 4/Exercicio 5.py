text="""The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you"""

text=text.replace(".","")
text=text.replace(",","")
text=text.replace(":","")
text=text.lower()
text=text.split()
palavra=str
total=[]


for x in text:
    for y in range(0,len(x)):
        if x[y]in "python" and palavra!=x and len(x)>4:
            palavra=x
            total.append(x)
          
print('Palavras',total,'\n\nNúmero de palavras:',len(total))