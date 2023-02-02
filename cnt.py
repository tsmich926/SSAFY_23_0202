#swa 연속된 1갯수세기
# for test_case in range(T):
#     N = int(input())
#     s = input()
#     cnt = 0
#     for i in range(len(s)):
#         if s[i] == 1:
#             cnt += 1

# TC = int(input())
# for test_case in range(1,TC+1):
    N = int(input())
    ai = list(input())
    print(ai)
    cnt = 0
    lst = []
    for i in range(len(ai)):
        cnt = ai.count(ai[i])
    #     lst.append(cnt)
    # print(lst)
    # mmax = max(lst)
    print (cnt,ai[i])
    

    # idx = lst.index(mmax)
    # print(idx)



ai = list(input())
print(ai)
cnt = 0
lst = []
for i in range(len(ai)):
    cnt = ai.count(ai[i])
    #     lst.append(cnt)
    # print(lst)
    # mmax = max(lst)
    print (cnt,ai[i])