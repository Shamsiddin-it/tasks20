# a = int(input())
# m = 1
# i = 1
# while m <= a:
#     print(" "*(a-m), end="")
#     for j in range(m):
#         print(i,"", end="")
#         i += 1
#     print()
#     m += 1


# 2
# a = int(input())
# while True:
#     if a==1:
#         print(a)
#         break
#     else:
#         print(f"{a},",end="")
#         if a%2==0:
#             a=a//2
#         else:
#             a=3*a+1
    


# 3
# def delitel(a):
#     mylist = []
#     for i in range(1,a//2 + 1):
#         if a%i==0:
#             mylist.append(i)
#     sum = 0
#     for i in mylist:
#         sum+=i
#     return a==sum

# a= int(input())
# i=1
# while i<=a:
#     if delitel(i):
#         print(i)
#     i+=1


# 4
# a = input()
# mydict = {}
# for i in a.lower():
#     mydict[i] = mydict.get(i, 0) + 1
# print(mydict)


# 5
# a = input()
# mydict = {}
# mylist = list(a.split())
# for i in mylist:
#     mlist = []
#     for j in range(len(mylist)):
#         if i == mylist[j]:
#             mlist.append(j)
#     if i not in mydict.keys():
#         mydict[i] = mlist
# print(mydict)
    

# 6
# mydict = {}
# old_dict = {'a':[1,2],
#             'b':[3,4]}
# for k,v in old_dict.items():
#     for i in v:
#         mydict[i]=k
# print(mydict)

# 7
# dict1 = {'a':1, 'b':2, 'c':3}
# dict2 = {'a':2, 'b':3, 'c':4}
# mydict = {}
# for k,v in dict1.items():
#     for m,n in dict2.items():
#         if m==k:
#             mydict[m] = v+n
# print(mydict)   

# 8
# a = input()
# mydict = {}
# mylist = list(a.split())
# for i in mylist:
#     cnt = 0
#     for j in range(len(mylist)):
#         if i == mylist[j]:
#             cnt+=1
#     if i not in mydict.keys():
#         mydict[i] = cnt
# print(mydict)

# 9
# a = int(input()) 
# for i in range(1, a+1):
#     print(" " * (a - i), end="")
#     for j in range(1, i + 1):
#         print(j, end="")
#     for j in range(i-1, 0, -1):
#         print(j, end="")
#     print()
# for i in range(a-1, 0, -1): 
#     print(" " * (a - i), end="")
#     for j in range(1, i + 1):
#         print(j, end="")
#     for j in range(i-1, 0, -1):
#         print(j, end="")
#     print() 


# 10
# def factorial(a):
#     if a>=1:
#         i =1
#         fact = 1
#         while i<=a:
#             fact *= i
#             i+=1
#     else:
#         fact = 1
#     return fact


# def sfc(a):
#     m = str(a)
#     sum = 0
#     for i in m:
#         n = int(i)
#         sum+=factorial(n)
#     return sum==a

# a= int(input())
# for i in range(1,a+1):
#     if sfc(i):
#         print(i)

# 11
# def xar(a):
#     m = str(a)
#     sum = 0
#     for i in m:
#         n = int(i)
#         sum+=n
#     return a%sum == 0

# a= int(input())
# for i in range(1,a+1):
#     if xar(i):
#         print(i)

# 12
# source_file = 'source.txt'
# numbered_file = 'numbered.txt'

# with open(source_file, 'r') as src, open(numbered_file, 'w') as numb:
#     line_number = 1
    
#     for line in src:
#         numb.write(f"{line_number}: {line}")
#         line_number += 1

# print("finished")


# 13
# n = int(input())
# with open("example.txt", "r", encoding='utf-8') as file:
#     lict = file.readlines()
#     for line in lict[-n:]:
#         print(line)


# 14
# with open("exampl2.txt", 'r', encoding='utf-8') as file1, open("ex3.txt", 'w', encoding='utf-8') as file2:
#     for i in file1:
#         file2.write(f'{i}')


# 15
# with open("file.txt", "r", encoding='utf-8') as file:
#     lict = file.readlines()
#     n = lict[0]

# new = n.split()
# ndict = {}
# for i in new:
#     ndict[i] = ndict.get(i, 0) + 1
# print(ndict)


# 16
# with open("file1.txt", "r", encoding='utf-8') as file:
#     mlist = file.readlines()
# for i in mlist:
#     if i == "\n":
#         mlist.remove(i)

# with open("file1.txt", 'w', encoding='utf-8') as file1:
#     file1.writelines(mlist)

# 17
# with open("newfile.txt", "r", encoding='utf-8') as file:
#     mlist = file.readlines()

# n = mlist[0]
# newl=n.split()
# for i in range(0, len(newl)):
#     if newl[i] == 'world':
#         newl[i]=' Python'

# with open("newfile.txt", 'w', encoding='utf-8') as file1:
#     file1.writelines(newl)


# 18
# with open("file3.txt", "r", encoding='utf-8') as file:
#     mlist = file.readlines()
# n = mlist[0]
# mlist2=n.split()
# cnt = 0
# for i in mlist2:
#     cnt+=1
# print(cnt)

# 19
# dict = {'apple':10,'banana':5, 'charry':15}
# newl = []
# for i in dict:
#     newl.append((i, dict[i]))
# for i in range(len(newl)):
#     for j in range(i + 1, len(newl)):
#         if newl[i][1] > newl[j][1]:
#             newl[i], newl[j] = newl[j], newl[i]
# dict2 = {}
# for item in newl:
#     dict2[item[0]] = item[1]
# print(dict2)

# 20
# mylist = [5,3,8,6,7]
# def Ziyodshavi(nlist):
#     for i in range(len(nlist)):
#         for j in range(i + 1, len(nlist)):
#             if nlist[i] > nlist[j]:
#                 nlist[i], nlist[j] = nlist[j], nlist[i]
#     return nlist

# def Kamshavi(nlist):
#     for i in range(len(nlist)):
#         for j in range(i + 1, len(nlist)):
#             if nlist[i] < nlist[j]:
#                 nlist[i], nlist[j] = nlist[j], nlist[i]
#     return nlist

# print(f"Ziyodshavi {Ziyodshavi(mylist)}")
# print(f"kamshavi {Kamshavi(mylist)}")