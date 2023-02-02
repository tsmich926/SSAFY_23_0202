# import sys
# sys.stdin = open("input.txt","r")
# T = 1
# lst  = []
# for k in range(1,T+1,1):
#     N = int(input())
#     hgt = list(map(int,input().split()))
#     for i in range(2,N-2):
#         right = hgt[i] - max(hgt[i+1],hgt[i+2])
#         left = hgt[i] - max(hgt[i-1],hgt[i-2])
#         if right > 0 and left > 0 :
#             jomang = (min(right,left))
#             lst.append(jomang)
#         print(lst)
#     sum = 0
#     for k in lst:
#         sum += k
#     print(f'#{k} {sum}')


# T = 1
# lst  = []
# for k in range(1,T+1,1):
#     N = int(input())
#     hgt = list(map(int,input().split()))
#     for i in range(2,N-2):
#         mmax = max(hgt[i+1],hgt[i+2],hgt[i-1],hgt[i-2])
#         jomang = hgt[i] - mmax
#         if  jomang > 0 : 
#             lst.append(jomang)
#         print(lst)
#     sum = 0
#     for k in lst:
#         sum += k
#     print(f'#{k} {sum}')

import sys
sys.stdin = open("input.txt","r")
lst  = []
for l in range(1, 11):
    N = int(input())
    hgt = list(map(int,input().split()))
    curmax = 0
    for i in range(2,N-2):
        if curmax < hgt[i+1]:
            curmax = hgt[i+1]
        elif curmax < hgt[i+2]:
            curmax = hgt[i+2]
        elif curmax < hgt[i-1]:
            curmax = hgt[i-1]
        elif curmax < hgt[i-2]:
            curmax = hgt[i-2]
        jomang = hgt[i] - curmax
        if  jomang > 0 : 
            lst.append(jomang)
    print(jomang)
    print(lst)
    sum = 0
    for k in lst:
        sum += k
    print(f'#{l} {sum}')

