import json
    #εισάγεται το αρχείο
file = open("dictionary.txt", "r")
contents = file.read()

dic = contents.split("\n")
        
Dict = {} 
for i in range(len(dic)):
    Dict[i] = json.loads(dic[i])

Keys = Dict[0].keys()
Items = Dict[0].items()
print (Keys)
print (Items)
print("Τα διαθέσιμα κλειδιά του αρχείου είναι:")
for x in Keys:
    print(x)
key = input("Ποιο από τα παραπάνω κλειδιά του αρχείου σας ενδιαφέρουν:")

separate = contents.split("\n")
print (len(separate))
value = []
for i in range(len(separate)):
    val = separate[i].split(",")
    
    for j in range(len(val)):
        value.append(val[j])
print ( value)

