def listcomp(x, y, z, n):
    coords = [[i, j, k] for i in range(x+1) 
                for j in range(y+1)
                for k in range(z+1)
                if sum([i,j,k]) != n]
    return coords

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(listcomp(x, y, z, n))