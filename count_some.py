class Solution:
    def count_some(starting_number: int, ending_number: int, k: int) -> int:
        count = 0
        for i in range(starting_number, ending_number):
            if (i % k == 0):
                count += 1

        return count

    