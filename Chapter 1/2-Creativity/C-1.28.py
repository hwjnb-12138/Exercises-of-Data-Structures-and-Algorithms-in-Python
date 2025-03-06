def norm(v, p=2):
    count = 0
    for data in v:
        count += data ** p
    res = count ** (1/p)
    return res

# def norm(v, p=2):
#     temp = sum(val ** p for val in v)
#     return temp ** (1/p)
