ss = range(1, 10)
es = range(10)
ns = range(10)
ds = range(10)
m = 1
os = range(10)
ys = range(10)
rs = range(10)

for s in ss:
    for e in es:
        for n in ns:
            for d in ds:
                for o in os:
                    for y in ys:
                        for r in rs:
                            if int(str(s) + str(e) + str(n) + str(d)) + int(str(m) + str(o) + str(r) + str(e)) == \
                                    int(str(m) + str(o) + str(n) + str(e) + str(y)) and [s, e, n, d, m, o, r, y] == \
                                    list(dict.fromkeys([s, e, n, d, m, o, r, y])):
                                print(int(str(s) + str(e) + str(n) + str(d)))
                                print(int(str(m) + str(o) + str(r) + str(e)))
                                print(int(str(m) + str(o) + str(n) + str(e) + str(y)))
