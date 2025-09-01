def removeZeros(s):
  while s and s[-1] == '0':
      s.pop()
  cleaned = []
  for p in s:
      p = p.rstrip('0')
      if p == "":
          continue
      cleaned.append(p)

  return ".".join(cleaned)

a = "2.020.0".split(".")

print(removeZeros(a))