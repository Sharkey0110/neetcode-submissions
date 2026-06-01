class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_num = -1

            for j in range(len(arr) -1, i, -1):
                num = arr[j]
                max_num = max(max_num, num)
            arr[i] = max_num
        
        return arr


