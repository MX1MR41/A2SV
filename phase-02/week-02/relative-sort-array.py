class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        d = {x:i for i,x in enumerate(arr2)}
        
        list1, list2 = [], []

        for i in arr1:
            if i in d:
                list1.append(i)
            else:
                list2.append(i)

        list1.sort(key = lambda x: d[x])
        list2.sort()

        list1.extend(list2)


        return list1
        