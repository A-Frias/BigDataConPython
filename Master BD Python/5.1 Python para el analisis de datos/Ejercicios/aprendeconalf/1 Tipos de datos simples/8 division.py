def division(n,m):
    if n<m:
        c=0
        r=n
    else:
        r=n%m
        c=n//m
    return "El resultado de dividir {} entre {} es {} y el resto es {}".format(n,m,c,r)

print(division(10,3))