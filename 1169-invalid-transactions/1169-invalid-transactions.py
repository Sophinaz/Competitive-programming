class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = []
        track = defaultdict(list)
        added = set()

        for idx in range(len(transactions)):
            tx = transactions[idx].split(',')
            time = int(tx[1])

            for j in range(time-60, time+61):
                if j in track:
                    for i in track[j]:
                        if i[0] == tx[0] and i[1] != tx[3]:
                            if idx not in added:
                                added.add(idx)
                                result.append(transactions[idx])
                            result.append(transactions[i[2]])
            if int(tx[2]) > 1000 and idx not in added:
                result.append(transactions[idx])
                added.add(idx)
            temp = [tx[0], tx[3], idx]

            track[time].append(temp)
        return list(result)