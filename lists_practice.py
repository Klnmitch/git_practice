# Lists Practice
k = [4, 15, -7]
print(k)

# .append is a pre-defined function that adds
k.append(1)  #adds "1" to the list
k.append("Hello!")  #adds "Hello!" to the list
k.append([1, 2, 3])  # adds another list to the list
print(k)

# .pop is a pre-defined function that removes the last item in the list
k.pop()
print(k)

#retrieving items from lists using [] - 0,1,2,3... represent the location in the lists
print(k[0]) #retrieves "4"
print(k[4]) #retrieves "Hello!"

#changing the value as well..
k[1] = 200 #this changes "15" to "200"
print(k)

# List exercise: Switch "4" with "Hello!" within the list
temp = k[0]
temp_2 = k[4]               #this was my way
k = [temp_2, 200, -7, 1, temp]
print(k)
#a better way to do it
temp = k[0]
k[0] = k[4]
k[4] = temp
print(k)
# AN EVEN BETTER WAY
k[0], k[4] = k[4], k[0]
print(k)

