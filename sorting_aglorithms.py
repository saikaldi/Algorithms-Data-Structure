# Bubble Sort
# How it works:

# Go through the array, one value at a time.
# For each value, compare the value with the next value.
# If the value is higher than the next one, swap the values so that the highest value comes last.
# Go through the array as many times as there are values in the array.


# So the Bubble Sort algorithm must run through the array again, and again,
# and again, each time the next highest value bubbles up to its correct position.

# An array with values to sort.
# An inner loop that goes through the array and swaps values if the first value is higher than the next value.
# This loop must loop through one less value each time it runs.
# An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.

# Example List: [4, 2, 3, 1]
# len(list1) = 4
# 1st Pass (i = 0)
# 🔹 range(len(list1) - i - 1) → range(4 - 0 - 1) → range(3)
# ✅ We compare:

# list1[0] with list1[1]
# list1[1] with list1[2]
# list1[2] with list1[3]
# ✔ The largest element moves to the last position.

# 2nd Pass (i = 1)
# 🔹 range(len(list1) - i - 1) → range(4 - 1 - 1) → range(2)
# ✅ We compare:

# list1[0] with list1[1]
# list1[1] with list1[2]
# ✔ The second-largest element moves to the second-last position.

# 3rd Pass (i = 2)
# 🔹 range(len(list1) - i - 1) → range(4 - 2 - 1) → range(1)
# ✅ We compare:

# list1[0] with list1[1]
# ✔ The third-largest element moves to the third-last position.

# After 3 passes (i = 3), the list is fully sorted, and no more comparisons are needed.


def bubble_sort(list1):

    for i in range(len(list1) - 1):  # n

        for j in range(len(list1) - i - 1):  # n
            if list1[j] > list1[j + 1]:  # c
                high = list1[j]  # c
                list1[j] = list1[j + 1]  # c
                list1[j + 1] = high  # c

    return list1  # c          n*n+c+c+c+c+c=n^2+5c=O(n^2)


print(bubble_sort([2, 1, 5, 2, 4, 9, 7, 56, 1, 4]))


# S=[n*(a1+an)]/2
# (n - 1) + (n - 2) + (n - 3) + ... + 1
# The outer loop runs n - 1 times, where n is the number of items in the list.
# The inner loop runs less with each outer loop iteration because the largest items are moved to their correct positions. Specifically:
# In the first iteration, the inner loop runs n - 1 times (since we’re comparing each adjacent pair).
# In the second iteration, it runs n - 2 times.
# In the third iteration, it runs n - 3 times.
# And so on, until the last iteration of the outer loop, which only runs once."


# a1 = (n - 1),  the last term a_n is 1.

# The number of terms is n - 1, because the series starts from (n - 1) and ends at 1. So we can substitute into the formula:
# S = n * (n-1) / 2 = n^2 -> O(n^2)


def bubble_sort2(list1):

    n = len(list1)
    swapped = True

    while swapped:
        swapped = False

        for i in range(n - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                swapped = True

    return list1


print(bubble_sort2([2, 6, 4, 1, 7]))
