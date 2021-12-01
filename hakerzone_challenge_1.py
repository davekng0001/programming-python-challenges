#need to remember what numbers have been looked at  before
#find out how many pairs are in the given array
#
#
#
#
#
#
#
#
count = 1
pairs = 0
ar = [10,20,20,10,10,30,50,10,20]
ar_trsh = []
check = False

for i in range(len(ar)):
    if len(ar_trsh) > 0:
        
        for l in ar_trsh:
            if ar[i] == l:
                check = True
        
        if check == True:
            check = False 
            print("continue ", ar[i])
            continue
        else:
            print("no trash keep it going")
        
    
    for j in range(i+1,len(ar)):
        print("j loop start: ", ar[j])
        if ar[i] == ar[j]: 
            count = count +1
            print("j loop ar[j == ar[i = ", ar[j])
            
    ar_trsh.append(ar[i])
            
    print("break  ", ar[i])
    if count > 0:
        print("pairs of ",ar[i], ": ", count)
        pairs = pairs + count//2
        count = 1
        
    # one less than last element in array
    if i == len(ar)-2:
        break
        
print("total pairs: ", pairs)
print("items in ar trs ", ar_trsh)