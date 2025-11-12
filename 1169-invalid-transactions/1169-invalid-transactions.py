class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        track = defaultdict(lambda: defaultdict(set))
        invalids = []

        for i in range(len(transactions)):
            # split into four 
            name, time , amount, place = transactions[i].split(',')
            # add them to hashmap
            track[int(time)][name].add(place)

        for transaction in transactions:
            isinvalid = False
            # split into four
            name, time, amount, place = transaction.split(',')
            # check if amount excedes 1000 
            if int(amount) > 1000:
                isinvalid = True

            # check for invalidity by place
            for ti in range(-60, 61):
                curr_time = int(time) + ti
                # if curr_time already exisits
                if curr_time in track:
                    if name in track[curr_time]:
                        if len(track[curr_time][name]) > 1 or (place not in track[curr_time][name]):
                            isinvalid = True

            # if invalid add to result
            if isinvalid:
                invalids.append(transaction)

        return invalids

