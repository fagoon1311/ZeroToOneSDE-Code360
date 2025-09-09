# Problem: Given a string and a pattern, find if the pattern exists in the string.

# Pre-requisite: KMP Algorithm
"""
KMP Algorithm:
Normally, if a mismatch happens, we restart checking the pattern from the beginning. This causes re-checking of characters again and again.

KMP is smart. It uses a helper table called LPS (Longest Prefix Suffix).

LPS tells us how much of the pattern is already matched and where we can safely continue from, instead of restarting.

In short:
If a mismatch happens, KMP doesn’t go back fully.
It "jumps" using the LPS table to avoid repeating work.

Steps:
Precompute the LPS array for the pattern.
(This array tells for each position in the pattern the length of the longest prefix which is also a suffix).

Use this LPS to decide how much to "shift" the pattern when a mismatch occurs.

This makes the search efficient → O(n + m) time, instead of O(n × m).
"""


def findPatternInString(string, pattern):
  # Precompute the LPS array for the pattern
  lps = [0] * len(pattern)
  i, j = 0, 1
  while j < len(pattern):
    if pattern[i] == pattern[j]:
      lps[j] = i + 1
      i += 1
      j += 1

    else:
      if i == 0:
        lps[j] = 0
        j += 1

      else:
        i = lps[i - 1]



findPatternInString("ababcabcabababd", "abcdabca")
