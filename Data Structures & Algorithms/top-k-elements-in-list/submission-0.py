class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_map = {}
        new_list = list()
        for i in nums:
            if i in new_map:
                new_map[i] += 1
            else:
                new_map[i] = 1
    
        for i in range(k):
            max_key = max(new_map, key=new_map.get)
            new_list.append(max_key)
            new_map.pop(max_key)
        return new_list
        
         
            