def groupAnagrams(strs):
    res=[]
    visited=[]
    for i in range(0,len(strs)):
        print("String[i]",strs[i],"Executed")
        # print("Result Array ",res)
        if strs[i] not in visited:
            ans=[]
            ans.append(strs[i])
            for j in range(i,len(strs)):
                # print("String[j]",strs[j])
                if i!=j and strs[j] not in visited:
                    print("Visited: ", visited)
                    if(sorted(strs[i])==sorted(strs[j])):
                        ans.append(strs[j])
                        visited.append(strs[j])
                        visited.append(strs[i])
            print("Temp Array ",ans)
            res.append(ans)       
    return res

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# More Faster Solution
# def groupAnagrams(self, strs):
#     d = {}
#     for w in sorted(strs):
#         key = tuple(sorted(w))
#         d[key] = d.get(key, []) + [w]
#     return d.values()