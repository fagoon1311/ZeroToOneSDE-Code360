#Problem Statement: Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

# If 'N = 4' and 'W = 10'. The weights and values of items are weights = [6, 1, 5, 3] and values = [3, 6, 1, 4]. 
#Then the best way to fill the knapsack is to choose items with weight 6, 1 and  3. The total value of knapsack = 3 + 6 + 4 = 13.00


# Solution: Greedy Approach.
# we can use a greedy approach to solve this problem. We will sort the items based on the value per weight ratio in descending order. Then we will iterate through the sorted items and add them to the knapsack until we reach the capacity. If the weight of the item is less than the remaining capacity, we will add the item to the knapsack. If the weight of the item is greater than the remaining capacity, we will add a fraction of the item to the knapsack.

# Time Complexity: O(nlogn) where n is the number of items. We are sorting the items based on the value per weight ratio.

def maximumValue(items, n, w):
  items.sort(key = lambda x: x[1]/x[0], reverse=True)

  total = 0.0

  for weight, value in items:
    if w == 0:
      break

    if weight <= w:
      total += value
      w -= weight

    else:
      total += value * (w/weight)
      w = 0

  # ITEMS contains [weight, value] pairs.
  return total