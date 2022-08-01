import math
#Quadratic Equation= ax^2+bx+c where a!=0
#a,b,c are coefficients
# Problem Statement says that we have to find the value of x
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))
dis=((b*b)-(4*a*c))
sq=math.sqrt(abs(dis))
#dis is discriminant
#As x has highest power of 2, so it will have 2 roots
r1= ((-b+sq)/(2*a))
r2= ((-b-sq)/(2*a))
if dis>0:
    print("roots are real & unequal",r1,r2)
elif dis==0:
    print("roots are equal", r1)
elif dis<0:
    imaginary=math.sqrt(-dis)/2*a
    r1=-b/2*a
    print("roots are imaginary",r1+imaginary,r1-imaginary)






