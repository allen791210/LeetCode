
def longestSubsequence(arr, difference):
    if not arr:
        return 0
    
    if difference < 0:
        arr.sort(reverse = True)
    else:
        arr.sort()
    
    arr_set = set(arr)
    visited = set()
    results = []

    for n in arr:
        if n in visited:
            continue
        target = n + difference
        sub_seq = [n]
        visited.add(n)
        while target in arr_set: 
            sub_seq.append(target)
            target += difference
            visited.add(target)
        if len(sub_seq) > len(results):
            results = sub_seq
    
    return results

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(longestSubsequence(arr, difference))