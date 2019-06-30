b=[[1,123456,3], [2,6,4],[13,19,100]]
MAX=0

for current_list in b:
 
    for current_number in current_list:
        if (current_number>MAX):
            MAX=current_number
    print(MAX)

