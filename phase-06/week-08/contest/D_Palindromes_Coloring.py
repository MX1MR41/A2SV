def max_shortest_palindrome():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    test_cases = []

    idx = 1
    for _ in range(t):
        n, k = map(int, data[idx].split())
        s = data[idx + 1]
        test_cases.append((n, k, s))
        idx += 2

    results = []
    for n, k, s in test_cases:
        
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ord('a')] += 1

        
        pairs = sum(count // 2 for count in char_count)
        odds = sum(count % 2 for count in char_count)

        
        max_length = 2 * (pairs // k)
        odds += 2 * (pairs % k)
        if odds >= k:
            max_length += 1

        results.append(max_length)

    print("\n".join(map(str, results)))

max_shortest_palindrome()