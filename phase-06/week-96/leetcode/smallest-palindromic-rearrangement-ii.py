class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)
        n = len(s)
        extra = ""

        for x in cnt:
            if cnt[x] % 2:
                extra = x
                cnt[x] -= 1
                n -= 1
            cnt[x] //= 2

        n //= 2

        # 1. Calculate the initial exact total permutations ONCE.
        current_total_perms = math.factorial(n)
        for x in cnt:
            if cnt[x] > 0:
                current_total_perms //= math.factorial(cnt[x])

        res = ""
        prev = 0

        for i in range(n):
            alpha = ""

            for l in range(ord("a"), ord("z") + 1):
                if cnt[chr(l)] > 0:
                    alpha += chr(l)

            prefix = []
            
            # The length BEFORE we place the next character
            rem = n - i 
            
            pre = prev

            for j in range(len(alpha)):
                # 2. THE MAGIC SHORTCUT:
                # Instead of dividing big factorials in a loop, we find the 
                # exact options in O(1) time using the math property!
                curr_options = current_total_perms * cnt[alpha[j]] // rem

                pre += curr_options
                prefix.append(pre)

            choice = -1
            for j in range(len(alpha)):
                if prefix[j] >= k:
                    choice = j
                    break

            if choice == -1 or k > prefix[-1]:
                return ""

            # 3. Update the total permutations for the next iteration based on our choice
            current_total_perms = current_total_perms * cnt[alpha[choice]] // rem
            cnt[alpha[choice]] -= 1

            prev = prefix[choice - 1] if choice > 0 else prev

            res += alpha[choice]

        res += extra + res[::-1]

        return res
