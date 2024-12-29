def solve_humanoid(t, test_cases):
    results = []

    for case in test_cases:
        n, h = case[0]
        astronauts = sorted(case[1])

        def simulate(h):
            # Initialize variables
            green_serums, blue_serums = 2, 1
            absorbed = 0
            i = 0

            while i < n:
                if astronauts[i] < h:
                    h += astronauts[i] // 2
                    absorbed += 1
                    i += 1
                elif green_serums > 0 or blue_serums > 0:
                    # Try using serums
                    if green_serums > 0:
                        green_serums -= 1
                        h *= 2
                    elif blue_serums > 0:
                        blue_serums -= 1
                        h *= 3
                else:
                    break

            return absorbed

        results.append(simulate(h))

    return results

if __name__ == "__main__":
    t = int(input())
    test_cases = []
    for _ in range(t):
        n, h = map(int, input().split())
        astronauts = list(map(int, input().split()))
        test_cases.append(((n, h), astronauts))


    results = solve_humanoid(t, test_cases)
    print("\n".join(map(str, results)))
