f = open("Όνομα αρχείου.txt", "r")  #εισάγεται το αρχείο txt
txt = f.read()  #το αρχείο εισάγεται στην μεταβλητή txt  
lenght = len(txt)   #υπολογίζεται ο αριθμός των χαρακτήρων 
letters = []
binaries = []

for i in range(lenght): #για κάθε χαρακτήρα
    j = txt[i]  
    letters.insert(i,j) 
    binary = int(format(ord(letters[i]), '07b'))    #φτιάχνεται η δυαδική απεικόνιση
    binary=str(binary)
    if len(binary)==6:
        binary="0"+binary
        binaries.insert(i,binary)
    elif len(binary)==7:
        binaries.insert(i,binary)

print("Η δυαδική απεικόνιση μήκος 7 ψηφίων φαίνεται παρακάτω:")
print(binaries)
        #στην μεταβλητή αυτή "ενώνονται" τα στοιχεία του πίνακα binaries
everystr = ""
for i in range(lenght):
    everystr = everystr + binaries[i]
print(everystr)
        
sum_0 = 0
sum_1 = 0 
max_0 = 0
max_1 = 0
           #ελέγχουμε για κάθε χαρακτήρα * 7 επειδή παρουσιάζεται με 7 bit
for i in range(lenght*7):
    if everystr[i] == "0":
        sum_0 = sum_0 + 1
        sum_1 = 0
        if sum_0 > max_0:
            max_0 = sum_0
    else:
        sum_1 = sum_1 + 1
        sum_0 = 0
        if sum_1 > max_1:
            max_1 = sum_1
            
print('Το πλήθος συνεχόμενων 0 είναι:',max_0)
print('Το πλήθος συνεχόμενων 1 είναι:',max_1)
print("Το πλύθος χαρακτήρων του αρχείου είναι:",lenght)
print('Αυτοί είναι οι χαρακτήρες του αρχείου:',letters)