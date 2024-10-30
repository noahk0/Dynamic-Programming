def coinChange(self, coins: List[int], amount: int) -> int:
    if not amount:
        return 0

    n, seen, new = 1, set(), [amount]

    while new:
        bfs, new = new, []

        while bfs:
            for c in coins:
                if c == bfs[-1]:
                    return n
                elif c < bfs[-1] and bfs[-1] - c not in seen:
                    seen.add(bfs[-1] - c)
                    new.append(bfs[-1] - c)

            bfs.pop()

        n += 1

    return -1
