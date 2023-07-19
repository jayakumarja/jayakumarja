file=open("jay.txt",'w')
file.write("jay")
file.close()

file=open("jay.txt",'r')
j=file.read()
print(j)

file=open("jay.txt",'a')
file.write("20 mail")
file.close()


