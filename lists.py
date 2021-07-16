if __name__ == '__main__':
    N = int(input())
    i=0
    result=[]
    while i<N:
        i+1
        arr = map(str, input().split())
        commands=list(arr)
        print(commands)
        if commands[0] == 'insert':
            a=int(commands[1])
            b=int(commands[2])
            result.insert(a,b)
            print(result)
        elif commands[0] == 'print':
            print(result)
        elif commands[0] == 'remove':
            a=int(commands[1])
            result.remove(a)
        elif commands[0] == 'append':
            a=int(commands[1])
            result.append(a)
            print(result)
        elif commands[0] == 'sort':
            result.sort()
        elif commands[0] == 'pop':
            result.pop()
        elif commands[0] == 'reverse':
            result.reverse()
        

