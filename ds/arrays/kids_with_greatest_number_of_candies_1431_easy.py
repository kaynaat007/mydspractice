from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:

      output = []
      max_candy = max(candies)
      for e in candies:
          if e + extraCandies >= max_candy:
              output.append(True)
          else:
              output.append(False)
      return output

candies = [2,3,5,1,3]

candies = [4,2,1,1,2]

candies = [12,1,12]

print(kidsWithCandies(candies, 10))



