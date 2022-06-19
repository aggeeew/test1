#迴圈
"""
range()整數串列
語法:range(起始值,終止值,間隔值)
*產生的串烈士從起始值到[終止值-1]的串列
"""

list1=range(5) #01234
print(list(list1))

list2=range(3,8) #34567
print(list(list2))

list3=range(3,8,2)
print(list(list3))

list4=range(8,3,-1)
print(list(list4))

list5=range(-2,4)
print(list(list5))

list6=range(8,3) #不顯示結果
print(list(list6))

#練習
list7=range(0,10)
print(list(list7))

list8=range(1,10)
print(list(list8))

list9=range(1,10,2)
print(list(list9))

list10=range(10,0,-2)
print(list(list10))

"""
for迴圈
固定次數的動作

語法:
for 變數 in 串列:
    程式區塊
"""
list11=["香蕉","蘋果","梨子"]
for s in list11:
    print(s)
#計算1+2...+10之和(for range)
sum =0
for i in range(1,11):
    sum += i
print(sum)

for n in range(3):
    print(n,end="")

#練習
A=int(input("請輸入正整數："))
for B in range (0,A+1,1):
    print(B,end="")

C=int(input("請輸入正整數："))
sum1=0
for D in range(1,C+1,1):
    sum1+=D
print("1到",C,"的整數和為",sum1)

E=int(input("請輸入加總開始值："))
F=int(input("請輸入加總終止值："))                                 
G=int(input("請輸入加遞增減值："))
sum2=0
for H in range(E,F,G):
    sum2+=H
    print("i為",H,"加總結果為",sum2)

#巢狀or迴圈
for i in range (1,6):
    print("外部迴圈",i,"次迴圈，內部執行",i,"次迴圈：",end="")
    for j in range(1,i+1):
        print("#",end="")
    print()

for i in range (1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

"""
#99乘法表(有錯)
for i in range(1,10):
    for j in range(1,10):
        product=i*j
        print("%d*%d=%2d " % (i,j,product),end="") 
    print()
"""

#練習
g=int(input("請輸入正整數："))
for i in range (1,g+1):
    for j in range (1,i+1):
        print(j,end="")
    print()

#運算子in
a=(1,2,3,4)
if 1 in a :
    print("數字1在tuple a 中")
else:
    print("數字1不在tuple a 中")

a=list("fdgdfgfdgfdfdgfdgfdfgfdgfda")
if 'a' in a:
    print("q在串列a裡")
else:
    print("q不在串列a裡")

lang1={"早安":"Good morning","謝謝":"Thank you"}
if "謝謝" in lang1:
    print("謝謝的英文為",lang1["謝謝"])
else:
    print("查不到英文的謝謝")

a=set("tiger")
if "t" in a:
    print("t在集合a裡")
else:
    print("t不在集合a裡")




