#x = 0                     #initialize x to equal zero 
#sum = 0                   #initialize sum to equal zero
#counter = 0               #initialize counter to equal zero

#while counter != 10:      #loop until the counter reaches 10 inputs
  #x = int(input())        #input an intiger
  #sum = sum + x           #add each input to the sum everytime it loops 
  #counter = counter + 1   #add one to the counter everytime an integer is                            inputted
#print(sum / counter)      #to get the average you divide the sum of the                                inputs by the number of inputs





#counter = 0
#sum = 0                    #initialize sum and counter

#while True:                #executes when true
    
  #number = int(input())    #user input
  #counter = counter + 1    #count number
  #sum = sum + number       #updates your sum
  #if counter == 10:        #waits for 10 inputs
    #break

#print(sum / counter)






#numberproduct = 0
#numbersum = 0
#numcount = 0

#inpu = (input("Please input a number, or press q to recieve the average and the product of your number \n"))

#while True:
  #inpu = (input("Please input a number, or press q to recieve your average number and total product \n"))
  #if inpu == "q":
    #print("The average of your numbers is :", numbersum / numcount)
    #break
  #numbersum = numbersum + int(inpu)
  #numcount = numcount + 1
  




#sum = 0
#count = 0
#product = 1
#print("press 'q' once you have completed entering the numbers")
#N = input()
#while N != 'q':
  #sum = sum + int(N)
  #count = count + 1
  #product = product * int(N)
  #N = input()
#print("your average is" ,sum/count, "and your product is", product)



#a = []               #decaire an object / initialize - empty list
#n = int(input("How long is your list? "))       #lenght of your list
                   
#for i in range(n):             
  #new_element = int(input("Number? "))   #ask for int
  #a.append(new_element)        
#print(a)                    #prints the entire list




#words = input().split()   #takes the input and makes a list of all the words by serparating them at the spaces

#for i in range(len(words)):   #loops for the amount of words in the list
  #first = words[i]   #makes a string for the ith word, i changes by 1 each iteration to cycle through all the words in the list
  #print(first[0], end='')   #prints the first character of the string (changes each iteration), and makes it so the next iteration it is printed right after it.

#pseudo code
#words = split string into a list
#for i in range(length of the list):
  #first = words[i]
  #print(first[0])