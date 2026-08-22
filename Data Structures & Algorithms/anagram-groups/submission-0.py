class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = {}
        cont = []
        new_strs = [''.join(sorted(word)) for word in strs]

        for i in range(len(new_strs)):
            if new_strs[i] not in ana_map:
                ana_map[new_strs[i]] = [strs[i]]
            else:
                ana_map[new_strs[i]].append(strs[i])
        
        for ana in ana_map:
            cont.append(ana_map[ana])

        return cont





        
