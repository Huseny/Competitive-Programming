class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        string = []
        for i in range(n):
            s = i + 1
            if s%3 == 0 and s % 5 == 0:
                string.append("FizzBuzz")
            elif s%3 == 0:
                string.append("Fizz")
            elif s%5 == 0:
                string.append("Buzz")
            else:
                string.append(str(s))
        return string
