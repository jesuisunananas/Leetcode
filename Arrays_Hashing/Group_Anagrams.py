def groupAnagrams(strs):
    anagrams = {}
    for i in strs:
        current_str = ''.join(sorted(i))
        if current_str not in anagrams:
            anagrams[current_str] = []
        anagrams[current_str].append(i)
    return anagrams.values()

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(groupAnagrams(["x"]))
print(groupAnagrams([""]))