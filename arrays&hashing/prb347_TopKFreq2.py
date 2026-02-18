class Solution:
    def topKFrequent(self, nums, k):
# -----------------------------------------
# STEP 1: Count how many times each number appears
# -----------------------------------------
# Example: nums = [1,1,1,2,2,3]
# count will become: {1:3, 2:2, 3:1}
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1


    # -----------------------------------------
    # STEP 2: Create buckets based on frequency
    # -----------------------------------------
    # Index = frequency
    # Value = list of numbers that appear that many times
    #
    # Why len(nums) + 1 ?
    # Because a number can appear at most len(nums) times
    #
    # Example after filling:
    # index: 0 1   2   3
    #       [] [3] [2] [1]
    #
        freq = [[] for _ in range(len(nums) + 1)]

        for number, frequency in count.items():
            freq[frequency].append(number)


    # -----------------------------------------
    # STEP 3: Traverse from highest frequency → lowest
    # -----------------------------------------
    # This avoids sorting (key idea of bucket sort)
        result = []

    # Start from max possible frequency
        for i in range(len(freq) - 1, 0, -1):

        # freq[i] contains numbers appearing i times
            for number in freq[i]:
                result.append(number)

            # Stop as soon as we collected k elements
                if len(result) == k:
                    return result

