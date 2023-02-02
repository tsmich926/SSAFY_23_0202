
# cnt[0] 0의 갯수
# cnt[1] 1의 갯수
# cnt의 공간은 가장큰값+1 (0부터 가장큰값까지의 갯수를 저장해야 하므로)
k = 4
N = 8
nums = [0,4,1,3,1,2,4,1]
res = [-1] * N
# res = [0,1,1,1,2,3,4,4]
# =>i 0 [1] 2 3 [4] [5] 6 7 [8]
counts = [0] * (k+1)
for num in nums:
    counts[num] += 1
print(counts)
for i in range(k):
    counts[i+1] = counts[i+1] + counts[i]
print(counts)

for i in range(N-1, -1,-1):
    num = nums[i]
    pos = counts[num]
    res[pos] = num
    counts[num] -= 1
print(res)
#안정정렬: 현재 데이터의 정보를 유지시키며 정렬

nums = [1,2,3,1,2]
cnt1 = 0
for num in nums:
    if num ==1:
        cnt1 += 1
    if num == 1:
        cnt2 += 1

""""""""""""""""""""""""
# <baby_gin>

s = input()
l = list(map(int(),s))

counts = [0] * 10
for num in l:
    counts[num] += 1
# print(counts)
i = 0
tri = 0
run = 0
while i<10:
    if counts[i] >= 3:
        counts[i] -= 3
        continue
    elif i<=7 and counts[i]>0 and counts[i+1]>0 and counts[i+2]>0:
        counts[i] -= 1
        counts[i+1] -=1
        counts[i+2] -=1
        run += 1
        continue
    i += 1


