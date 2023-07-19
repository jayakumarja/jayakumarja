##file=open("jay.txt",'w')
##file.write(" hi iam jay hi\n")
##file.close()
##
##
##file=open("jay.txt",'r')
##j=file.read()
####print(j)



name="jay"
age=23
mail="jay8524@gmail.com"
file=open("jay.txt",'a')
file.write(f"{name} {age} {mail}\n")
file.close()


