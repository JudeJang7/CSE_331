from Card import *
import re


class PokerHand:
    def __init__(self, iterable):
        self.cards = set(iterable)

    def __repr__(self):
        return repr(self.cards)

    @classmethod
    def from_string(cls, s):
        cards = [Card.from_symbol(s) for s in re.findall(r'[0-9ATJQK][cdhsCDHS]', s)]
        return cls(cards)

    @staticmethod
    def deal_hands(deck, num_hands, hand_size=5):
        return [PokerHand(it) for i, it in zip(range(num_hands), *[iter(deck)] * hand_size)]

    def __eq__(self, other):
        return self.cards == other.cards

    def is_straight(self):
        ranks = set(c.rank for c in self.cards)

        def is_rooted_at(r):
            return all(i in ranks for i in range(r, r + 5))

        return any(is_rooted_at(r) for r in ranks)

    def is_flush(self):
        from collections import defaultdict

        suit_counts = defaultdict(lambda: 0)
        for c in self.cards:
            suit_counts[c.suit] += 1
        return len(suit_counts) == 1

    def is_straight_flush(self):
        # doesn't handle 7 card hands
        return self.is_flush() and self.is_straight()

    def get_kinds(self):
        from collections import defaultdict
        rank_counts = defaultdict(lambda: 0)
        for c in self.cards:
            rank_counts[c.rank] += 1
        return rank_counts

    def is_k_of_a_kind(self, k):
        return any(v == k for v in self.get_kinds().values())

    def is_full_house(self):
        return self.is_k_of_a_kind(3) and self.is_k_of_a_kind(2)

    def is_two_pair(self):
        counts = self.get_kinds().values()
        return len(list(filter(lambda c: c == 2, counts))) == 2

    def order_kinds(self):
        kinds = [(m, k) for (k, m) in self.get_kinds()]
        sorted(kinds, reverse=True)  # sorted isn't in place
        return [k for (m, k) in kinds for _ in range(m)]

    def __lt__(self, other):
        """
        Determines if this PokerHand is ranked lower than the other PokerHand.
        :type other: PokerHand
        """
        def helper(f1, f2):
            if not f1:
                return True
            elif not f2:
                return False
            else:
                k1 = self.order_kinds()
                k2 = other.order_kinds()
                return k1 < k2

        if self.is_straight_flush() or other.is_straight_flush():
            return helper(self.is_straight_flush(), other.is_straight_flush())
        elif self.is_k_of_a_kind(4) or other.is_k_of_a_kind(4):
            return helper(self.is_k_of_a_kind(4), other.is_k_of_a_kind(4))
        elif self.is_full_house() or other.is_full_house():
            return helper(self.is_full_house(), other.is_full_house())
        elif self.is_flush() or other.is_flush():
            return not self.is_flush()
        elif self.is_straight() or other.is_straight():
            return helper(self.is_straight(), other.is_straight())
        elif self.is_k_of_a_kind(3) or other.is_k_of_a_kind(3):
            return helper(self.is_k_of_a_kind(3), other.is_k_of_a_kind(3))
        elif self.is_two_pair() or other.is_two_pair():
            return helper(self.is_two_pair(), other.is_two_pair())
        elif self.is_k_of_a_kind(2) or other.is_k_of_a_kind(2):
            return helper(self.is_k_of_a_kind(2), other.is_k_of_a_kind(2))
        else:
            return helper(self.is_k_of_a_kind(1), other.is_k_of_a_kind(1))

    def __gt__(self, other):
        return not (self < other)
