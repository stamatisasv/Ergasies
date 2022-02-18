from urllib.request import Request, urlopen
import json

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

opap = Request('https://api.opap.gr/draws/v3.0/1100/last-result-and-active', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
kino = urlopen(opap).read()
kino = kino.decode()
kino = json.loads(kino)
kino = kino["last"]
kino = kino["winningNumbers"]
kino = kino["list"]

print(data)                     
middata = str(data)
finaldata = middata[33:97]          
print ('Η σειρά του randomness είναι:',finaldata)
pairs = []
ints = [] 
duos = []

j = 0 
print ('Τα ζεύγη που προκύπτουν είναι τα εξής:')
for i in range (32):  
    a = (finaldata[j:j+2])
    pairs.insert (i,a)
    j = j + 2
print (pairs)
j = 0
print ('Από την μετατροπή σε ακεραίους προκύπτουν τα εξής:')
for i in range (32):
    a = (int(finaldata[j:j+2],16))   
    ints.insert (i,a)
    j = j + 2
print(ints)
j = 0       
print ('Μετά την πράξη modulo 80 έχουμε τα εξής:')
for i in range (32):  
    a = ((int(finaldata[j:j+2],16))%80)
    duos.insert(i,a)
    j = j + 2
print(duos)
                #ταξινόμηση λίστας

duos.sort() 
print ("Η λίστα μετά από την αύξουσα ταξινόμηση της:")
print (duos)
j = 31

                #αφαίρεση ίδιων αριθμών

for i in range (j):  
    end = "True"
    if i+1 >= j:
        break 
    while end == "True":
        if duos[i] == duos[i+1]:
            duos.pop(i+1)
            j = j - 1
        elif duos[i] != duos[i+1]:
            end = "False"
print ("Η λίστα μετά την αφαίρεση των ίδιων αριθμών:")
print (duos)
print ("Οι τελευταίοι αριθμοί που κληρώθηκαν στο κίνο είναι οι εξής:")           
print (kino)
for i in range (20):
    for j in range (len(duos)):
        if kino[i] == duos[j]:
            print("Ο αριθμός",duos[j],"από τoυς τυχαίους αριθμούς κληρώθηκε στο κίνο")