#lex_auth_01269446319507046499

def remove_duplicates(value):
    s=value.replace(" ","")
    last_occ = {}
    stack = []
    visited = set()
    print(value)

    for i in range(len(s)):
        last_occ[s[i]] = i
    print(last_occ)

    for i in range(len(s)):

        if s[i] not in visited:
            while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                visited.remove(stack.pop())

            stack.append(s[i])
            visited.add(s[i])
    print(stack)
    return ''.join(stack)
    #start writing your code here

print(remove_duplicates("tigerwas drinking water"))
