T = int(input())
for test_case in range(1, T + 1):
	N = int(input())
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
	print(f'#{test_case} {maxV} {maxI})


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
