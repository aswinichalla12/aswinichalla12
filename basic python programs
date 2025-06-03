#python programs using conditional statements.
#1 to print even no.s
n=int(input("Enter n value:"))
for i in range(2,n,2):
    print(i,end=" ")
#2 to print odd no.s
n=int(input("Enter n value:"))
for i in range(1,n,2):
    print(i,end=" ")
#3
if 4:
    print("hello")
    if 3:
        print("hi")
#4
if 0:
    print("hello")
    if 3:
        print("hi")
#5
for i in range(5): # 0 1 2 3 4 
    for j in range(5): #0 1 2 3 4 
        print(i,j,end=" ")
    print() #goes to new line i.e for i loop
#6      
n=1
print("even" if n%2==0 else "odd")
#7 factorial
n=5
fact=1
for i in range(2,n+1):
    fact*=i
print(fact)
#8 o sum digits in a number
n = 123    #123%10=3 #123//10=2 #12//10=1 #1//10=0
sum=0
while n:
	sum+=n%10
	n//=10
print(sum)
#9 to find length
n=4595
count=0
while n:
	n//=10
	count+=1
print(count)
#10 armstrong
n=4595
count=0
temp=n
while n:
	n//=10
	count+=1
sum=0
n=temp
while n:
    single=n%10
    sum+=single**count
    n//=10
print("arm" if temp==sum else "not arm")
#11fib(to print particular Fibonacci number)
n=6
if n<=1:
    print(n)
else:
    first=0
    second=1
    for i in range(n-1):
        third=first+second
        first=second
        second=third
print(third)
#12 palindrome
n=123
#123%10=3(res)
#123//10=12
#3*10=30+12%10=32
#32*10=320+1=321
n=12121
res=0
temp=n
while n:
    rem=n%10
    res=(res*10)+rem
    n//=10
print("palindrome" if res==temp else "not palindrome")
#13 prime or not
n=5
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print("prime" if count==2 else "not a prime")
#method-2
n=15
count=0
for i in range(2,n):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime")
#method-3
n=6
count=0
for i in range(2,n//2):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime")
#method-4
n=6
count=0
for i in range(2,(n//2)+1):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime")
#14
r=20
for n in range(2,r+1):
    for i in range(2,(n//2)+1):
        if n%i==0:
            break
    else:
        print(n)
#15 to add even digits in a number
n=98762
count=0
while n:
    rem=n%10
    if rem%2==0:
        count+=rem
    n=n//10
print(count)
#16 to add prime digits in a number
n=987464
count=0
while n:
    rem=n%10
    if rem in [2,3,5,7]:
        count+=rem
    n=n//10
print(count)
#Python programs using data types
#17 to print even no. in list
a=[1,2,3,4,5,6]
for i in a:
    if i%2==0:
        print(i)
#18 to print negative no. in list
a=[1,-2,3,-4,5,6]
for i in a:
    if i<0:
        print(i)
#19 to print reverse no. in list
a=[1,-2,3,-4,5,6]
for i in range(len(a)-1,-1,-1):
    print(a[i])
#20 to print reverse index in list
a=[1,-2,3,-4,5,6]
for i in range(len(a)-1,-1,-1):
    print(i)
#21 to print odd no. in list
a=[1,-2,3,-4,5,6]
for i in range(0,len(a),2):
    print(a[i])
#22 to print even no. in list
a=[1,-2,3,-4,5,6]
for i in range(1,len(a),2):
    print(a[i])
#23 moving zeros to last
a=[1,2,0,3,0,4,5]
for i in a:
    if i==0:
        a.remove(0)
        a.append(0)
print(a)
#24 to print min no.
a=[1,2,1,3,0,4,5]
search=a[0]
for i in range(1,len(a)):
    if search>a[i]:
        print(a[i])
#25 to print max no.
a=[1,2,3,4,5,10]
search=a[0]
for i in range(1,len(a)):
    if a[i]<search:
        search=a[i]
print(a[i])
#26 to print min no.
a=[1,0,2,3,4,5,10]
search=a[0]
for i in range(1,len(a)):
    if a[i]<search:
        search=a[i]
print(search)
#27 to delete duplicates
#method-1
a=[1,0,2,3,3,4,5,10]
print(set(a))
#method-2
a=[1,0,2,3,3,4,5,10]
res=[] #to create empty list
for i in a:
    if i not in res:
        res.append(i)
print(res)
#28 to count no. of times a value is present
a=[1,3,2,5,3,2,2]
res={} #to create empty dictionary
for i in a:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
print(res)
#29 to sum of postive and negative values
a=[1,3,2,-5,-4]
pos=0
neg=0
for i in a:
    if i>0:
        pos+=i
    else:
        neg+=i
print([pos,-neg])
#30 to remove vowels
a="abijoajk"
res=" "
for i in a:
    if i not in "aeiou":
        res+=i
print(res)
#31 to print only vowels
a="abijoajk"
res=" "
for i in a:
    if i in "aeiou":
        res+=i
print(res)
#ORD: ord converts alphabet into ascii
#CHR: chr converts ascii into alphabet
#32 
a="aikhofj"
res=""
for i in a:
    if i in "aeiou":
        res+=chr(ord(i)-32)
    else:
        res+=i
print(res)
#33 to print the addition of range of alphabets
a="abc"
res=0
for i in a:
    res+=ord(i)-96
print(res)
#34 to print 1 to n using while
n=int(input())
i=1
while i<=n:
    print(i)
    i+=1
#35 to print n to 0
n=10
for i in range(n+1,0,-1):
    print(i)
#36 print only single digit
li=[1,12,3,24,5,53]
for i in li:
    if i<10:
        print(i)
#37 add only single digit
li=[1,12,3,24,5,53]
count=0
for i in li:
    if i<10:
        count+=i
print(count)
#38 to print a number if sum of that number and its index is even
l=[1,3,2,4]
for i in range(len(l)):
    sum= l[i]+i
    if sum%2==0:
        print(l[i])
#39 to print only capital letters
l="aAbBcC"
for i in l:
    if ord(i)>=65 and ord(i)<97:
        print(i)
#40 to print only small letters
l="aAbBcC"
for i in l:
    if ord(i)>=97 and ord(i)<=122:
        print(i)
#41 to print only digits
a="jk78687jrt"
for i in a:
    if ord(i) in range(48,58):
        print(i)
#42 to print only alphabets
a="ghj437688"
for i in a:
    if ord(i) in range(65,91) or ord(i) in range(97,123):
        print(i)
#43 sum of odd index values and even index values
a=[1,2,3,4,5,6]
odd_sum=0
even_sum=0
for i in range(len(a)):
    if a[i]%2==0:
        even_sum+=a[i]
    else:
        odd_sum+=a[i]
print(even_sum)
print(odd_sum)
if even_sum>odd_sum:
    print("even")
else:
    print("Odd")
#44 to print present index+next index value
a=[1,2,3,1,5]
start=0
while start<len(a):
    print(a[start])
    start=start+a[start]
#45 to sum until it is single digit
n=12345
while n>=10:
    sum=0
    while n:
        sum+=n%10
        n//=10
    n=sum
print(n)
#46 to print digits and alp separately
a="nbjh6678nbj"
num=alp=""
for i in a:
    if ord(i) in range(48,58):
        num+=i
    else:
        alp+=i
print(num,alp)    
#47 to check n is in the table of a
n=int(input())
a=int(input())
if n%a==0:
    print(f"{n} is in the table of {a}")
else:
    print(f"{n} is not in the table of {a}")
#48 from 0th index increaing value count n=1234557 and return output as 5
n=12343
n=str(n)
prev=0
for i in range(len(n)):
    if prev>=int(n[i]):
        break
    prev=int(n[i]) 
else:
    i+=1
print(i)
#49 to print rank
a=2
b=3
c=1
if a>b and a>c:
    if b>c:
        print("a1 b2 c3")
    else:
        print("a1 c2 b3")
elif b>c:
    if a>c:
        print("b1 a2 c3")
    else:
        print("b1 c2 a3")
else:
    if a>b:
        print("c1 a2 b3")
    else:
        print("c1 b2 a3")
#50 missing sequence
a=[1,2,3,4,5]
b=[1,2,4,5]
for i in range(len(b)):
    if a[i]!=b[i]:
        print(i)
        break
else:
    print(i+1)   
#51 to return even in sorted and odd in any order
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
for i in range(len(even)):
    for j in range(len(even)-1):
                if even[j]>even[j+1]:
                    even[j],even[j+1]=even[j+1],even[j]
result=even+odd
print(result)
#52 sum of other two elements
a=[1,2,3]
res=[a[1]+a[2],a[0]+a[2],a[0]+a[1]]
print(res)
#53 to check password is valid or not 
def verification(a):
    alp=dig=sym=up=lo=False
    if not (8<=len(a)<=10):
        return False
    for i in a:
        if i.isalpha():
            if i.isupper():
                up=True
            else:
                lo=True 
        if i.isdigit():
            dig=True
        if i in "@_":
            sym=True
    if sym and dig and up and lo:
        return True
    return False           
a=input()
print(verification(a))
#54 pan verification
pan=input()
print(len(pan)==10 and pan[:5].isalpha() and pan[:5].isupper() and pan[5:-1].isdigit() and pan[-1].isalpha() and pan[-1].isupper())
