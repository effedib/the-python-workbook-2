import math
s1 = float(input('Enter the length of the first side of the triangle:'))
s2 = float(input('Enter the length of the second side of the triangle:'))
s3 = float(input('Enter the length of the third side of the triangle:'))
s = (s1+s2+s3)/2
A = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print('The area of the triangle is',A)