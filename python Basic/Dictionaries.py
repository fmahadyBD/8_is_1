# oder does not metter
d={"Fahim":1722003285,"Hasan":1580645628,"Mahady":1981822261}
print(d)
print(d["Fahim"])
#add new
d["bby"]=111111
print(d)
#delete
del d['bby']
print(d)

for key in d:
    print("Key:",key ,"Value:",d[key])
    
    
# using Tuples
print()

for k,v in d.items():
    print("Key:",k ,"Value:",v)
# find the key is exist in dictioonaries not not 
print("Mahady" in d)


# find the length of dictionaries
print("The lenght of Dictionaries:" ,len(d))

##access key and values:

print("Keys: ",d.keys())
print("Value:",d.values())
## update dictionaray:

d['Fahim']=0
print(d)
# delete everything:
d.clear()
print(d)