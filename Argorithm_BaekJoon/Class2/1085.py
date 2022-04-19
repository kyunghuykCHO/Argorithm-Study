# (0,0) (w,0) (0,h) (w,h) 인 직사각형이 있다.
# 한수는 현재 x y 에 위치해 있다
# 한수가 직사각형 경계선까지 가는 거리의 최솟값을 구하라

x,y,w,h = map(int,input().split())

a = x-0
b = y-0
c = w-x
d = h-y

print(min(a,b,c,d))