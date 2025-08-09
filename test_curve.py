from sfc import gen_curve


def bfs(curve):
    i = j = n = 0
    while n < curve.size - 1:
        if i + 1 < curve.shape[0] and curve[i + 1][j] == curve[i][j] + 1:
            i += 1
            n += 1
        elif i > 0 and curve[i - 1][j] == curve[i][j] + 1:
            i -= 1
            n += 1
        elif j + 1 < curve.shape[1] and curve[i][j + 1] == curve[i][j] + 1:
            j += 1
            n += 1
        elif j > 0 and curve[i][j - 1] == curve[i][j] + 1:
            j -= 1
            n += 1
        else:
            return False
    return True


search_dim = 1000

for width in range(1, search_dim):
    for height in range(1, search_dim):
        try:
            z = gen_curve(width, height, "d_neg")
            if z.size > 0:
                if not bfs(z):
                    print(f"Failed Z-type curve with dimensions w={width}, h={height}")
                    quit()
        except:
            print(f"Failed Z-type curve with dimensions w={width}, h={height}")
            quit()
        try:
            g = gen_curve(width, height, "s_0")
            if g.size > 0:
                if not bfs(g):
                    print(f"Failed G-type curve with dimensions w={width}, h={height}")
                    quit()
        except:
            print(f"Failed G-type curve with dimensions w={width}, h={height}")
            quit()
