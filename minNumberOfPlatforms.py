# Problem Statement: Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of platforms required for the railway station so that no train waits.



# Solution1: The main idea behind this approach is to use an array, 'PLATFORMS', to store the number of platforms required at different points of time. Now, since the time range is from 0 to 2359 in the 24 hour format, we declare the array 'PLATFORMS' with a size of 2360 (as we need values from 0 to 2359) and all values initialized to 0.
''' 
    Time Complexity : O(N * 2360)
    Space Complexity :  O(1)

    Where 'N' is the number of trains.
'''


def calculateMinPatforms(at, dt, n):

    # Array to store the number of platforms required at different points of time.
    platforms = [0 for i in range(2360)]

    # Variable to store the final answer i.e. minimum number of platforms required.
    minNumOfPlatforms = 1

    for i in range(n):

        # Increment number of platforms for all times between arrival and departure (both inclusive).
        for j in range(at[i], dt[i]+1):
            platforms[j] += 1

            # Update minimum number of platforms.
            minNumOfPlatforms = max(minNumOfPlatforms, platforms[j])

    # Return the minimum number of platforms.
    return minNumOfPlatforms




# Solution2: The main idea behind this approach is to consider all the events in the sorted order. Once the events are in the sorted order, we find the number of trains at any time by keeping track of the trains that have arrived but not yet departed. The minimum number of platforms required will be the maximum number of trains at any time.

''' 
    Time Complexity : O(N * log(N))
    Space Complexity :  O(1)

    Where 'N' is the number of trains.
'''


def calculateMinPatforms1(at, dt, n):

    # Sort both the arrays.
    at.sort()
    dt.sort()

    # Indicates the number of platforms needed at a time.
    curNumOfPlatforms = 0

    # Variable to store the final answer i.e. minimum number of platforms required.
    minNumOfPlatforms = 0

    i, j = 0, 0

    while (i < n and j < n):

        # If the next event in sorted order is arrival, increment count of platforms needed.
        if (at[i] <= dt[j]):
            curNumOfPlatforms += 1
            i += 1

        # Else decrement count of platforms needed.
        else:
            curNumOfPlatforms -= 1
            j += 1

        # Update minimum number of platforms.
        minNumOfPlatforms = max(minNumOfPlatforms, curNumOfPlatforms)

    # Return the minimum number of platforms.
    return minNumOfPlatforms

# Solution3: The main difference between this approach and the previous one is that instead of looping through the 'PLATFORMS' array for every train, we just increment the number of platforms at the time of arrival and decrement the number of platforms after the departure of every train. Just like the previous approach, we use an array, 'PLATFORMS', to store the number of platforms required at different points of time. Now, since the time range is from 0 to 2359 in the 24 hour format, we declare the array 'PLATFORMS' with a size of 2361 (as we need values from 0 to 2360) and all values initialized to 0.

def calculateMinPatforms2(at, dt, n):
  # Write your code here.
  pl = [0] * 2361
  r = 0
  res = 0
  i = j = 0
  while i < len(at) and j < len(dt):
      pl[at[i]] += 1
      pl[dt[j] + 1] -= 1
      i += 1
      j -= 1

  for i in range(len(pl)):
      r += pl[i]
      res = max(r, res)

  return res