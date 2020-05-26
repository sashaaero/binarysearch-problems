r = 0

a = 0
b = 10

while b < 2**31:
    r = 0
    for i in range(a, b):
        s = str(i)
        if '2' in s:
            r += 1
    print('for %d: %d' % (len(str(b)), r))
    a = b
    b *= 10
