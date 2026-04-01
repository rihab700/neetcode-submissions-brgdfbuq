class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        anagram = {}
        for st in strs:
            sorted_str = "".join(sorted(st))
            if sorted_str in anagram:
                anagram[sorted_str].append(st)
            else:
                anagram[sorted_str]= [st]
        return list(anagram.values())