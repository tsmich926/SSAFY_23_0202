# 최대한 이동할 수 있는 정류장 수 K
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동
# 충전기가 설치된 M개의 정류장 번호

# 최대한 3정류장이동
# 10번까지 이동
# 충전기가 설치된 정류장은 

# 1 3 5 7 9 일때

#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 1번에서 충전
# 3번
# 5번

# 충전소
# 1 3 7 8 9
# 1번 충전
# 3번충전 
# 7번까지 못가서 0나옴

# 충전소 
# 4 7 9 14 17

T = int(input())
for test_case in range(1, T + 1):
    K, N, M = int(input())
    nums = list(map(str,input()))
    # counts = [0] * (N+1)
    for i in range(N):
        0 + K 

""""""""""""""""""
TC = int(input())
for t in range(1,TC+1):
    K, N, M = map(int,input().split())
    CHS = list(map(int,input().split()))

    curV = 0
    cnt = 0
    while curV < N:
        #다음 충전위치를 찾는다
        nextV = curV + K
        if nextV in CHS:
            curV = nextV
            cnt +=1
        else: #nextV not in CHS:
            while curV < nextV and nextV not in CHS:         #다음정류장을 앞으로 이동하면서 충전기 찾음,
                nextV -= 1
            #2. 못찾은 경우 )curV와 curV+K 사이에 충전기가 없음
            if curV == nextV :
                #못감
                cnt = 0
                break #while 빠져나옴
            #충전 찾은 경우
            curV = nextV
            cnt += 1
    print(cnt)




