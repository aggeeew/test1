#練習
g=int(input("請輸入正整數："))
for i in range (1,g+1):
    for j in range (1,i+1):
        print(j,end="")
    print()

f=int(input("請輸入正整數："))
for i in range(f+1,0,-1):
    for j in range(1,i-1):
        print("*",end="")
    print()


#break範例
for i in range(1,11):
    if (i==4):
        break
    print(i,end=",")
print()


#continute範例
for i in range (1,11):
    if (i==4):
        continue
    print(i,end=",")
print()


#練習
k=int(input("請輸入正整數:"))
for i in range(1,k+1):
    if(i%5==0):
        continue
    print(i,end="")
print()