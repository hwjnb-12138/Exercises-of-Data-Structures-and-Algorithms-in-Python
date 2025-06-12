# A sequence S contains n−1 unique integers in the range [0,n−1], that
#  is, there is one number from this range that is not in S. Design an O(n)
# time algorithm for finding that number. You are only allowed to use O(1)
#  additional space besides the sequence S itself.

# calculate the sum of S,then calculate the sum of [0,n−1], the difference between these two sum is the missing number
