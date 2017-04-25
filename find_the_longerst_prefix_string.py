#返回最长公共字符串python3----byliulu
#情形一：只存在唯一的一个最长公共字符串
#输入： aaabbc aabcaaabbc aabbccaaab
#输出： ['aabbc']
#情形二：存在多个长度相同的最长公共字符串
#输入： abcd abbc abcde
#输出：['bc', 'ab']
strs=list(input().split())
#1、找到列表里最短的字符串
shorter=strs[0]
for i in strs[1:]:
    if len(i)<len(shorter):
        shorter=i
#2、找到最短字符串的所有子串，存在数组shortList中
m=0
n=len(shorter)
shortList=[]
while(m<n):
    i=n-m
    while(i>=0):
        shortList.append(shorter[m:m+i])
        i-=1
    m+=1
#3、shortList中去重复、删除空字符
for s in shortList:
    if s == '':
        shortList.remove(s)   
shortList=list(set(shortList))
#4、shortList列表中哪些元素在strs全部元素中，将其放入res结果中
res=[]
for item in shortList:
    count=0
    for x in strs:
        if item in x:
            count=count+1
    if count==len(strs):
        res.append(item)
#5、找出res中最长的元素并打印,若存在多个相同长度的字符串，就将它们全部打印出来
long=res[0]
for i in res[1:]:
    if len(i)>len(long):
        long=i
final=[]        
for i in res:
    if len(i)==len(long):
        final.append(i)
print(final)