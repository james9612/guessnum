import random
r = random.randint(1,100)
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


