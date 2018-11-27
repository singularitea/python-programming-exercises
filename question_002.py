# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

print('Enter your factorial:')
print('')
f = input()
fa = 1
if f == 0:
    print(0)
else:
    for i in range(1,int(f)):
        fa += fa*i

print(fa)
