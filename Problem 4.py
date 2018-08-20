#Find the largest palindrome possible by multiplying two three digit numbers
print(max(i*j for i in range(1,1000) for j in range(1,1000) if str(i*j) == str(i*j)[::-1]))


#print
#maximum of following arguments
# i times j for i between 1 and 1000
# for j between 1, 10000
# if (palindrome) 