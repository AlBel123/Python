list=[7, 7, 9, 10, 10, 4, 1]
def Count_Occurrences(list):
    #read in and assign the number to be searched for in the list
    num = int(input("Please enter a number to search for:"))
    count = 0#initialise variable count
    for i in list: #iterate over list
        if i == num:#if value is found 
            count+= 1 #add one to count
    return count
 
#print the number of times the number was found in the list
print("Number Searched for Occurs ", Count_Occurrences(list), " times in the list.")





minimum=list[0]
for currentNum in list[1:]:
    if (currentNum<minimum):
        minimum=currentNum

print("The minimum temperature was "+str(minimum))



maximum=list[0]
for currentNum in list[1:]:
    if (currentNum>maximum):
        maximum=currentNum

print("The maximum temperature was "+str(maximum))