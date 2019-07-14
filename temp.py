# coding:utf-8
'''
str = '11111222222222233333333344444444444444'
i = 0
j = 0
c = [1]
num = [str[0]]
print(len(str))
# 最长的连续相同数字以及他的长度
for i in range(len(str)-1):
    if str[i] == str[i+1]:
        c[j] += 1
        i += 1
    else:
        j += 1
        num.append(str[i+1])
        c.append(1)
        continue
print(num)
print(c)
# 计算连续数字最长的长度
for i in range(len(c)):
    maxnum = c[0]
    if c[i]>maxnum:
        maxnum = c[i]
    else:
        maxnum = maxnum
print(maxnum)
'''
# 冒泡排序
l = [1, 22, 33, 44, 0, 4, 5, 2, 15, 12, 99, 9, 8, 4]

y = len(l)
for i in range((len(l)-1)):
    a = 0
    for i in range((y-1)):
        if l[i] < l[i+1]:
            a = l[i+1]
            l[i+1] = l[i]
            l[i] = a
    y -= 1
print(l)
