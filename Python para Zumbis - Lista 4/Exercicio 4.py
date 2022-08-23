#Exercicio 4

txt = '''The Python Software Foundation and the global Python community welcome and encou rage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''

txt=txt.replace('.',' ')
txt=txt.replace(',',' ')
txt=txt.replace(':',' ')
txt=txt.lower()
txt=txt.split()
                
for x in txt:
  if x[0] in 'python' or x[-1] in 'python':   
    print(x)