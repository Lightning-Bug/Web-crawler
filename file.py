fin = open('try.txt', 'w')
fin.write("Iam the only one \n")
fin.write("Just have a loook at it")
fin.close()


fr = open('try.txt','r')
text = fr.read()
print(text)
fr.close()