# for i in range(1):
#     dump = int(input())
#     boxes = list(map(int,input().split()))
#     Min_b = boxes[0]
#     Max_b = boxes[0]
#     while dump != 0:
#         for box in boxes:
#             if box < Min_b:
#                 Min_b = box
#             if box > Max_b:
#                 Max_b = box
#             Max_b = Max_b - 1
#             Min_b = Min_b + 1
#             dump -= 1
#     print(Min_b,Max_b)


#? 리스트에서 최댓값과 최솟값을 구하는 함수
boxes =[1,2,3,4,5,6,7,8,9,10]
def mymin_fucn(boxes):
    Min_b = boxes[0]
    Max_b = boxes[0]
    for box in boxes:
        if box < Min_b:
            Min_b = box
        if box > Max_b:
            Max_b = box
    return Min_b,Max_b

minV, maxV = mymin_fucn(boxes)
print(minV, maxV)

for test_case in range(1, 10):
    dump = int(input())
    boxes = list(map(int,input().split()))
    while dump != 0:
        minV, maxV = mymin_fucn(boxes)
        new_idx1 = boxes.index(minV)
        new_idx2 = boxes.index(maxV)
        boxes[new_idx1] += 1
        boxes[new_idx2] -= 1
        dump -= 1

#? 리스트에서 최댓값과 최솟값을 구하는 함수
boxes =[1,2,3,4,5,6,7,8,9,10]
def mymin_fucn(boxes):
    Min_b = boxes[0]
    Max_b = boxes[0]
    for box in boxes:
        if box < Min_b:
            Min_b = box
        if box > Max_b:
            Max_b = box
    return Min_b,Max_b

# minV, maxV = mymin_fucn(boxes)
# print(minV, maxV)

# for test_case in range(1, 10):
#     dump = int(input())
#     boxes = list(map(int,input().split()))
#     while dump != 0:
#         minV, maxV = mymin_fucn(boxes)
#         new_idx1 = boxes.index(minV)
#         new_idx2 = boxes.index(maxV)
#         boxes[new_idx1] += 1
#         boxes[new_idx2] -= 1
#         dump -= 1
