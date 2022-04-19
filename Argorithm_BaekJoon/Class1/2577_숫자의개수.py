numberlist = []
multipeled = 1
for i in range(3):
    multipeled *= int(input())
multipeled = str(multipeled)

for i in range(0,10):
    print(multipeled.count("{}".format(i)))
