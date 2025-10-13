from typing import List
# Problem Statement: Given a list of intervals representing the start and end time of 'n' meetings, find the maximum number of meetings that can be performed in a meeting room.

# Solution1: he idea is to create a struct array MEETING of size ‘N’, where each entry of MEETING will have three elements: meeting number, the start time of the meeting, the end time of the meeting.
# Sort the MEETING array in increasing order of end time.
# Select the first meeting of the sorted MEETING as your first meeting also maintain one variable, say currentTime, to maintain the current allotted time. Initialize currentTime with end time of first meeting picked.
# Now iterate through the rest of the MEETING array from left to right and for each MEETING[i], check if it is possible to organize that meeting or not. If the start time of the MEETING[i] is greater than the currentTime, means it is possible to organize MEETING[i], then increase your answer by 1 and update currentTime with the end time of MEETING[i].
# Return your answer.

'''
Time Complexity: O(nlogn) where n is the number of meetings.
Space Complexity: O(n)

'''

def maximumMeetings(start: List[int], end: List[int]) -> int:
    meetings = [(i, start[i], end[i]) for i in range(len(start))]  # n 

    meetings.sort(key=lambda x: x[2]) #nlogn
    res = 0
    currTime = meetings[0][2]
    for i in range(1, len(meetings)): #n
        if meetings[i][1] > currTime:
            res += 1
            currTime = meetings[i][2]

    return res + 1


