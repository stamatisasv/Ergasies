import random
sumb_points = 0
sumw_points = 0
for j in range(100):
    
    
    b_points = 0
    w_points = 0
    
        #white tower y = w_t_y
        #white tower x = w_t_x

    #Τοποθέτηση Άσπρου Πύργου
    
    w_t_x = (random.randrange(1,9))
    w_t_y = (random.randrange(1,9))
     
    place_w_t = (w_t_x,w_t_y)
    print ('White tower is placed at:',place_w_t)

    #τοποθέτηση Άσπρου Αξιωματικού
    a = 0
    while a == 0 :
        #white officer y = w_o_y
        #white officer x = w_o_x
        
        w_o_x = (random.randrange(1,9))
        w_o_y = (random.randrange(1,9))
        
        place_w_o = (w_o_x,w_o_y)
        if place_w_o != place_w_t :
            a = 1
    print ('White officer is placed at:',place_w_o)
    

    #τοποθέτηση Μάυρης Βασίλισσας

    b = 0
    while b == 0 :
        #black queen y = b_q_y
        #black queen x = b_q_x 
        b_q_y = (random.randrange(1,9))
        b_q_x = (random.randrange(1,9))
        place_b_q = (b_q_x,b_q_y)
        if ((place_b_q != place_w_o) and (place_b_q != place_w_t)) :
            b = 1
    print ('Black queen is placed at:',place_b_q)

    #έλεγχος εάν ο πύργος τρώει την Βασίλισσα στην ιδια ευθεια καθετα με τον αξιωματικό 
    
    
    if ((w_t_x == b_q_x) and (w_o_x == b_q_x)):  
    
       if ((b_q_y > w_t_y) and (w_t_y > w_o_y)) : 
           w_points = w_points + 1  
           
       if ((b_q_y < w_t_y) and (w_t_y < w_o_y )) :
           w_points = w_points + 1
           
    elif ((w_t_x == b_q_x) and (w_o_x != b_q_x)):
        w_points = w_points + 1
           
        
    #έλεγχος εάν ο πύργος τρώει την Βασίλισσα στην ιδια ευθεια οριζοντια με τον αξιωματικό     
    if ((w_t_y == b_q_y) and (w_o_y == w_t_y)):  
        
        if ((b_q_x > w_t_x ) and (w_t_x > w_o_x )) : 
           w_points = w_points + 1 
        
        if ((b_q_x < w_t_x ) and (w_t_x < w_o_x )):
            w_points = w_points + 1
            
    elif (w_t_y == b_q_y):  
        w_points = w_points + 1        

    #έλεγχος εάν ο αξιωματικός τρώει την Βασίλισσα και ειναι διαγωνια με τον πυργο   

    for i in range(8):
        if place_w_o == (w_t_x-i,w_o_y-i):
            break
            
        elif  place_w_o == (b_q_x-i,b_q_y-i): 
                w_points = w_points + 1
                break
        if place_w_o == (w_t_x+i,w_o_y+i):
            break
        elif  place_w_o == (b_q_x+i,b_q_y+i): 
                w_points = w_points + 1
                break
        if place_w_o == (w_t_x-i,w_o_y+i):
            break
        elif  place_w_o == (b_q_x-i,b_q_y+i): 
                w_points = w_points + 1
                break
        if place_w_o == (w_t_x+i,w_o_y-i):
            break
        elif  place_w_o == (b_q_x+i,b_q_y-i): 
                w_points = w_points + 1
                break
    sumw_points = w_points + sumw_points
    if w_points == 0 :
        
         #έλεγχος εάν η βασιλισσα τρώει τον αξιωματικό στην ιδια καθετο
    
        if (b_q_x == w_o_x):  
            b_points = b_points + 1
         
         #έλεγχος εάν η βασιλισσα τρώει τον αξιωματικό στην ιδια οριζοντια
         
        if (b_q_y == w_o_y) :
            b_points = b_points + 1
            
         
        for i in range(8):
            if place_b_q == (w_t_x-i,w_o_y-i):
                 
                    b_points = b_points + 1
                    
            if place_b_q == (w_t_x+i,w_o_y+i):
                 
                    b_points = b_points + 1
                    
            if place_b_q == (w_t_x-i,w_o_y+i):
                 
                    b_points = b_points + 1
                    
            if place_b_q == (w_t_x+i,w_o_y-i):
                 
                    b_points = b_points + 1
                
  
            
    #Εμφάνιση πόντων
        print("white player's points is/are:",w_points)        
        print("black player's points is/are:",b_points)
    
        sumb_points = b_points + sumb_points
print("The sum of white player's points are:",sumw_points)
print("The sum of black player's points are:",sumb_points)