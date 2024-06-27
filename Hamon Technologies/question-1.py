# Corrected version of the code

def f(s):
    r = {}
    for i in s:
        if i in r:
            r[i] += 1
        else:
            r[i] = 1 # here corrected
    return r

# print(f("praneeth"))