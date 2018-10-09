input_string = input()

limit = len(input_string)
count = 0
for i in range(limit):
    if(input_string[i] == 'Q'):
        #print("Q")
        for j in range(i+1,limit):
            if(input_string[j] == 'A'):
                #print("QA")
                for k in range(j+1,limit):
                    if(input_string[k] == 'Q'):
                        count += 1
                        #print("QAQ")
print(count)