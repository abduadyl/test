
''' Function to find index in pref_sum vector upto which
all prefix sum values are less than or equal to val '''

def findInd(pref_sum, n, val):

    # Starting and ending index of search space

    start = 0
    end = n - 1

    # To store required index value. By default its -1

    res = -1

    ''' If middle value is less than or equal to val then
    index can lie in [mid + 1...n] else it lies in [0...mid - 1] '''

    while start <= end:
        mid = (start + end) // 2
        if pref_sum[mid][0] <= val:
            res = mid
            start = mid + 1

        else:
            end = mid - 1

    return res

# Function to find largest subarray having
# sum greater than or equal to 0
def largestSub(arr, n):

    # Length of largest subarray
    maxlen = 0

    # Vector to store pair of prefix sum
    # and corresponding ending index value
    pref_sum = []

    # To store the current value of prefix sum.
    res = 0

    # To store minimum index value in range
    # [0 ... i] of pref_sum vector
    min_index = [None] * (n)

    # Insert values in pref_sum vector
    for i in range(0, n):
        res = res + arr[i]
        pref_sum.append([res, i])

    pref_sum.sort()

    # Update min_index array
    min_index[0] = pref_sum[0][1]

    for i in range(1, n):
        min_index[i] = min(min_index[i - 1], pref_sum[i][1])

    res = 0
    for i in range(0, n):
        res = res + arr[i]

        # If sum is greater than or equal 0, then
        # answer is i + 1
        if res >= 0:
            maxlen = i + 1

        # If sum is less than 0, then find if there is a prefix array
        # having sum that needs to be added to current sum to make its value greater or equal to 0.
        # If yes then compare length of updated subarray with maximum length found so far

        else:
            ind = findInd(pref_sum, n, res - 1)
            if ind != -1 and min_index[ind] < i:
                maxlen = max(maxlen, i - min_index[ind])

    return maxlen

# -----------------------------Test function----------------------------:

arr_1 = [-1, -1, 1, -1, 1, 0, 1, -1, -1]
arr_2 = [1, 1, -1, -1, -1, -1, -1, 1, 1]

n_1 = len(arr_1)
n_2 = len(arr_2)
print(largestSub(arr_1, n_1))
print(largestSub(arr_2, n_2))
