from typing import List


class Solution:

  def leastInterval(self, tasks: List[str], n: int) -> int:

    ans = []
    obj = {}

    for i, task in enumerate(tasks):
      # print(i, task)
      if task not in obj:
        obj[task] = 1
      else:
        obj[task] += 1

    # for key in obj.keys():
    #   print('key %s, number %d' % (key, obj[key]))

    innerCount = 0
    tookTask = {}

    counter = 0

    # while len(obj.keys()) > 0:
    while len(obj.keys()) > 0 and counter < 100:
      counter += 1
      # print('len %d' % len(obj.keys()))

      if innerCount <= n:
        keys = list(obj.keys())

        for key in keys:
          # print('key %s %d' % (key, obj[key]))
          if innerCount > n:
            break

          if key not in tookTask:
            innerCount += 1
            tookTask[key] = 1
            ans.append(key)
            obj[key] -= 1

        for key in keys:
          # print('check key %s' % key)
          if obj[key] <= 0:
            # print('delete %s' % key)
            del obj[key]

        if len(obj.keys()) > 0:
          if innerCount < n + 1:
            # print('append %d' % (n - innerCount))
            for i in range(innerCount, n + 1):
              innerCount += 1
              ans.append('idle')

      else:
        tookTask = {}
        innerCount = 0

    print(ans)

    return len(ans)


my = Solution()
# tasks = ["A", "A", "A", "B", "B", "B"]
# # n = 2
# n = 0
# n = 50

tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
right = 16

tasks = [
    "A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F", "G", "G", "H",
    "H", "I", "I", "J", "J", "K", "K", "L", "L", "M", "M", "N", "N", "O", "O",
    "P", "P", "Q", "Q", "R", "R", "S", "S", "T", "T", "U", "U", "V", "V", "W",
    "W", "X", "X", "Y", "Y", "Z", "Z"
]
n = 2
right = 52

ans = my.leastInterval(tasks, n)
print("ans", ans)
print(ans == right)
