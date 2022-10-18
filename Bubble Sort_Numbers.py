numbs = [3,5,7,4,6,1,2]                                                   # list declaration

def bubble_sort(numbs):                                                   # function definition for sortation and passing array as parameter 
    numbs_len = len(numbs)                                                # get the length of the array
    for i in range(numbs_len-1):                                          # loop through the array to access the characters even to the last one
        flag = 0                                                          # declare a flag variable to check if a swap has occured
        for j in range(0, numbs_len-i-1):                                 # create a loop to compare each element of the array till the last one
            if numbs[j] > numbs[j+1]:                                     # if first character is greater than second character
                numbs[j+1], numbs[j] = numbs[j], numbs[j+1]               # swap positions
                flag = 1
                if flag == 0:                                             # break out of loop at 0
                    break
    return numbs                                                          # return ordered characters of the array
print("The numbers sorted in increasing order are: ", bubble_sort(numbs)) # print out ordered list 