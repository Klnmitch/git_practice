#for loops practice
k = ["strawberry", "cherry", "uber" ]
for element in k:
    print(element)
    print(element)

m = [21, 10, 13]
total = 0
for d in m:
    total = total + d
print(total)

# FInd the sum of 1, 2, 3, 4 using the range function
 # range(1, 5)  #finds the range of 1-5, not including 5
c = list(range(1, 5))
print(c)

#using it in a for loop
for i in range(1, 5):
    print(i)

#finding the total
total2 = 0
for i in range(1, 5):
    total2 = total2 + i
print(total2)
# or an easier way
total3 = 0
for i in range(1, 5):
    total3 += i
print(total3)

total4 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total4 += i
print(total4)

#Practice excercise: Compute all multiples of 3, 5
# that are less than 100
#_multiples = 6
#for m in range(1, 100):

#print(_multiples)
#I got this wrong, but here's the solution

total5 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total5 += i
print(total5)








