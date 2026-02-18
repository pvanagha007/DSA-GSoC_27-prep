## Reflections on each problem solved this week (Feb 1-7)


# Problem 217: Contains Duplicate

* Use Hashset
* Append if doesn't exist in the set.
* Hashsets = Lists


# Problem 219: Contains Duplicate II

* Instead use dictionary
* Key is always the number and the value is always the frequency
* Use enumerate() to make nums to a list


# Problem 242: Valid Anagram

* Can use in built libraries
* Sort both strings and count freq
* Store freq in dicts
* Check if freq matches


# Problem 1: Two Sum

* Enumerate nums
* Compute the difference
* Check whether the difference exists in list
* If not, add to dict
* Return a dict of list -> but only list


# Problem 49: Group Anagrams

* Use dicts
* Key is the sorted index of the list
* Value is the actual word in the list
* If match found, append to dict of list
* Or else, create a new key:value pair 


# Problem 347: Top K Frequency Elements

* Use list
* Bucket sort 
* Add nums to a dict 
* Key is number, value is frequency
* Append it to a list where index of list is the freq
* Traverse list in reverse order to get highest freq
* Stop the loop when len(res)==k


# Problem 238: Product of Array except self

* Use a single list
* Multiply ele with prf -> mult with prev ele
* Do the same for postfix but with the latter
* In the same list, must multiply pof and prf
* Prf-> from 0 to len
* Pof-> from len-1 to -1 : reverse order



