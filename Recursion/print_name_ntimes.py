from jsonschema import RefResolutionError


def rec(s,n):
    if n==1:
        print(s)
        return
    else:
        print(s)
        rec(s,n-1)
    pass
rec("sam",5)