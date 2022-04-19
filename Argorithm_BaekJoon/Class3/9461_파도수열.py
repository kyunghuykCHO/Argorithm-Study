T = int(input())
Nlist = []
for _ in range(T):
    Nlist.append(int(input()))
    maxval = max(Nlist)

wave = [1,1,1,2,2]
cnt = 0
for i in range(maxval-5):
    a = wave[cnt]
    b = wave[-1]
    wave.append(a+b)
    cnt+=1
for j in Nlist:
    print(wave[j-1])