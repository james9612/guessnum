import random
start = input('請隨機輸入範圍起始數')
end = input('請隨機輸入範圍最終數')
start = int(start)
end = int(end)
r = random.randint(start,end)
while True:
    ans = input('請猜數字:')
    ans = int(ans)
    if r == ans:
        print('你答對了')
        break
    elif ans > r:
        print('比答案大')
    elif ans < r:
        print('比答案小')
