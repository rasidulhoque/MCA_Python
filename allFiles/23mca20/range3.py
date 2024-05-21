rows=3
for i in range(0,rows+1):

    for j in range(i,0,-1):
        print(2**(j-1),"\t", end='')
    print("\n")
