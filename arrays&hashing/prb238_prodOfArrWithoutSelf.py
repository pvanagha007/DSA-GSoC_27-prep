class Solution:
    def productExceptSelf(self, nums):
# We will build the answer directly in this array.
# res[i] will eventually contain product of all elements except nums[i]
        res = [1] * len(nums)


    # ---------------------------------------------------
    # PASS 1 — Prefix products (left side multiplication)
    # ---------------------------------------------------
    # prf = product of all elements to the LEFT of current index
    #
    # Example nums = [1,2,3,4]
    # After this loop:
    # res = [1, 1, 2, 6]
    #        ^  ^  ^  ^
    #       no 1 1*2 1*2*3
    #
        prf = 1
        for i in range(len(nums)):
            res[i] = prf
            prf *= nums[i]


    # ---------------------------------------------------
    # PASS 2 — Postfix products (right side multiplication)
    # ---------------------------------------------------
    # pof = product of all elements to the RIGHT of current index
    #
    # We multiply the existing prefix value with postfix value
    #
    # Continuing example:
    # prefix result = [1,1,2,6]
    #
    # Traverse backwards and multiply:
    # final result = [24,12,8,6]
    #
        pof = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= pof
            pof *= nums[i]

        return res