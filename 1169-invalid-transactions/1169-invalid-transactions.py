class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        track = defaultdict(lambda: defaultdict(set))

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)
            track[time][name].add(city)

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)

            if amount > 1000:
                invalid.append(transaction)
                continue

            for timerange in range(time-60, time+61):
                if timerange in track and name in track[timerange]:
                    if len(track[timerange][name]) > 1 or city not in track[timerange][name]:
                        invalid.append(transaction)
                        break

        return invalid