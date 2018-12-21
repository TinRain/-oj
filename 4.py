def Num(n):
  if n==1:
    return 2
  else:
    return 3*Num(n-1) + 2
if __name__ =='__main__':
    n=int(input().strip())
    print(Num(n))