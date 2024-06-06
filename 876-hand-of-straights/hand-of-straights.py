class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        scount = sorted(count.keys())

        for key in scount:
            if count[key] > 0:
                start_count = count[key]

                for i in range(key, key + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count

        return True