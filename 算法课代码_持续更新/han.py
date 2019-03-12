def hanoi(n, left, mid, right, come, to):
    if n == 1:
        if come == mid or to == mid:
            # print('将',n,'从',come,'移动到',to)
            return 1
        else:
            # print('将', n, '从', come, '移动到', mid)
            # print('将', n, '从', mid, '移动到', to)
            return 2

    else:
        num1 = hanoi(n-1,left,mid,right,come,to)
        # print('将', n, '从', come, '移动到', mid)
        num2 = hanoi(n-1,left,mid,right,to,come)
        # print('将', n, '从', mid, '移动到', to)
        num3 = hanoi(n-1,left,mid,right,come,to)
        # print(num1,num2,num3)
        return num1+num2+num3+2


if __name__ == '__main__':
    while True:
        n = input()
        come = 'left'
        depend = 'mid'
        to = 'right'
        if n == '' or n == '0':
            continue
        else:
            number = int(n.split()[0])
            print(hanoi(number, come, depend, to, come, to))


