# for test_case in range(1,TC+1):
#     N = int(input())
#     ai = input()
#     count = [0] * 10
#
#     for i in range():
#         for k in range(2,N):
#             while i < N :
#                 if ai[i] == ai[k]:
#                     count += 1
#                     i += 1
#             print(ai)

# TC = int(input())
# for test_case in range(1,TC+1):
#     N = int(input())
#     ai = input()
#     cnt = [0] * 10
#     print(type(cnt))
#
#     for i in range(ai):
#         cnt = ai.count(i)

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
"""     maxV = 0
    for i in range(k+1):
        if maxV <= counts[i]:
            maxV = counts[i]
            maxI = i
    print(f'#{test_case} {maxI} {maxV} ')
"""

