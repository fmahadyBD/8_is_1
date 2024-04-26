#only read
with open('a.txt','r') as file:
    data=file.read()
    print(data)
#write:

with open('a.txt','w') as file:
    file.write("HI")


#append if file not exist then it will create:
with open('x.txt','a') as file:
    file.write('fahim')



    