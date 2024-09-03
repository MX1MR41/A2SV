class Solution:
    def getLucky(self, s: str, k: int) -> int:
        curr = []

        for i in s:
            temp = list(str(ord(i) - 96))
            curr.extend(temp)

        while k:
            curr = sum(map(int, curr))

            curr = list(map(int, str(curr)))

            k -= 1

        return int("".join(map(str, curr)))
