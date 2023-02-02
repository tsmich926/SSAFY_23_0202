# def counting_sort(arr):
#     max_arr = max(arr)
#     count = [0] * (max_arr+1)
#
#     for i in arr:
#         count[i] += 1
#     for i in range(max_arr + 1 ):
#         for _ in range(count[i]):

c = [0] * (k+1)
for i in range(0, len(A)):
    c [A[i]] += 1
for i in range(1, len(c)):
    c[i] += c[i-1]