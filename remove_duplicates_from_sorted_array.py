class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # must be done in place
        # take in list of integers
        # remove duplicates
        # return new length of list, and list as N, nums = [], nums need to be sorted in ascending

        array = nums
        array.sort()
        array_length = len(array)
        duplicate = array[0]
        for number in range(1, array_length-1):
            if array[number] == duplicate:
                array.pop(number)
                array_length = len(array)
                continue
            else:
                duplicate = array[number]

        print(len(array), f', nums = {array}')
