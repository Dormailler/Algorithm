def solution(n, l, r):

    if n == 0:
        return min(r, 1) - max(l - 1, 0)

    # Calculate the length of the string after n iterations
    length = 1 * (5 ** n)

    # Function to count the number of 1's in a given range
    def count_in_range(l, r, length, depth):
        if depth == 0 or l > length or r < 1:
            return 0
        if l <= 1 and r >= length:
            # Calculate the total number of 1's at this depth
            return (4 ** depth)

        mid = length // 2 + 1
        total_count = 0

        # Count 1's in the left half (originally 1 -> 11011)
        if l <= mid:
            total_count += count_in_range(l, min(mid, r), length // 5, depth - 1)

        # Count 1's in the right half (originally 1 -> 11011)
        if r > mid:
            total_count += count_in_range(max(1, l - mid), r - mid, length // 5, depth - 1)

        # If the middle position is in range, count it (it's always 1)
        if l <= mid <= r:
            total_count += 1

        return total_count

    return count_in_range(l, r, length, n)
