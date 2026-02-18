#my solution with help from gpt
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1    #store it in the dict with key as number and value as frequency
            d2=sorted(freq, key=freq.get, reverse=True)[:k]  #sort in descending order

        for i in range(0,k):
            return list(d2)[:k]  #return a list of dict keys in the range k