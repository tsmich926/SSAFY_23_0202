# ai = list(input())
# print(ai)
# cnt = 0
# lst = []
# for i in range(len(ai)):
#     cnt = ai.count(ai[i])
#     lst.append(cnt)
#     print(lst)
#     mmax = max(lst)
# print(mmax)
# num = ai.index(mmax) #숫자
# print(ai[num])

# 0123456789

# 4885
# N = input()
# ai = int(input())
# count = [0] * (max(ai) + 1)

# for num in ai:
#     count[num] += 1
# print(count)


# arr = int,input()

# count = [0] * (max(arr) + 1)

# for num in arr:
#     count[num] += 1
    
# print(count)
""""""""""""""""""""""""

s = '23856'
nums = list(map(int,s))
counts = [0] * 10
for n in nums:
    counts[n] += 1

#print(counts)
maxV = 0
for i in range(20):
    if maxV <= counts[i]:
        maxV = counts[i]
        maxI = i
print(maxV, maxI)

# for n in counts:
#     if maxV < n :
#         maxV = n
# print(maxV,counts.index(maxV))


##
maxI = 0
for i in range(10):
    if counts[maxI] <= counts[i]:
        maxI = i  
##다른방법

""""""""""""""""""""""""""""""
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(str,input()))
    k = 0
    for num in nums:
        if int(num) > k :
            k = int(num)

    counts = [0] * (k+1)
    print(counts)

    for n in nums:
        counts[int(n)] += 1

#print(counts)
    maxV = 0
    for i in range(k+1):
        if maxV <= counts[i]:
            maxV = counts[i]
            maxI = i
    print(f'#{test_case} {maxI} {maxV} ')