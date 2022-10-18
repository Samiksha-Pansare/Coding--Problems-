def minWindow(s: str, t: str) -> str:
    for i in range(0,len(t)):
        if t[i] not in s:
            print(t[i])
            return ""
    char_dict = {}
    for character in t:
        char_dict[character] = -1
    for j in range(0,len(s)):
        if s[j] in t:
            print(char_dict)
            char_dict[s[j]]=j
    min_index = min(char_dict.values())
    max_index = max(char_dict.values()) + 1
    return s[min_index:max_index]
print("Hello")
print(minWindow("A","AA"))
print("Hello")