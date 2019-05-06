#!/usr/bin/python3

import unittest

from Card import *
from Poker import *


class PokerTests(unittest.TestCase):
    def test_from_str(self):
        exp = PokerHand([
            Card(Rank.Ace, Suit.Club),
            Card(Rank.Queen, Suit.Diamond),
            Card(Rank.Seven, Suit.Heart)])
        hand = PokerHand.from_string('ACQD7H')
        self.assertEqual(exp, hand)

    def test_from_str2(self):
        exp = PokerHand([
            Card(Rank.Ten, Suit.Spade)
        ])
        hand = PokerHand.from_string('10S')
        self.assertEqual(exp, hand)

    def test_eq(self):
        self.assertEqual(PokerHand.from_string('ACQD7H4D3S'), PokerHand.from_string('4D3SAC7HQD'))
        self.assertNotEqual(PokerHand.from_string('ACQD7H4D3S'), PokerHand.from_string('ADQD7H4D3S'))
        self.assertNotEqual(PokerHand.from_string('ACQD7H4D3S'), PokerHand.from_string('3CQD7H4D3S'))

    def test_is_straight(self):
        self.assertTrue(PokerHand.from_string('2H3C4D5S6H').is_straight())
        self.assertFalse(PokerHand.from_string('2H3C4D5S7H').is_straight())
        self.assertTrue(PokerHand.from_string('2H3C4D5SAH').is_straight())
        self.assertTrue(PokerHand.from_string('AH2H3H4H5H').is_straight())
        self.assertTrue(PokerHand.from_string('10HJCQDKSAH').is_straight())

    def test_is_flush(self):
        self.assertTrue(PokerHand.from_string('2H3H4H5HAH').is_flush())
        self.assertTrue(PokerHand.from_string('2H3H4H7HAH').is_flush())
        self.assertFalse(PokerHand.from_string('2H3H4S5HAS').is_flush())
        self.assertFalse(PokerHand.from_string('2H3H4S5HAH').is_flush())

    def test_is_straight_flush(self):
        self.assertTrue(PokerHand.from_string('AH2H3H4H5H').is_straight_flush())
        self.assertFalse(PokerHand.from_string('2H3H4H5H7H').is_straight_flush())
        self.assertFalse(PokerHand.from_string('2H3C4D5S6H').is_straight_flush())
        self.assertTrue(PokerHand.from_string('10HJHQHKHAH').is_straight_flush())

    def test_get_kinds(self):
        hand = PokerHand.from_string('4H4C7S7DJD')
        kinds = hand.get_kinds()
        self.assertEqual({Rank.Four: 2, Rank.Seven: 2, Rank.Jack: 1}, kinds)

    def test_is_full_house(self):
        self.assertFalse(PokerHand.from_string('4H4C7S7DJD').is_full_house())
        self.assertTrue(PokerHand.from_string('4H4C7S7D4D').is_full_house())

    def test_is_two_pair(self):
        self.assertTrue(PokerHand.from_string('4H4C7S7DJD').is_two_pair())
        self.assertFalse(PokerHand.from_string('4H4C7S7D4D').is_two_pair())

    def test_order_simple(self):
        # Hands ordered from best to worst
        hands = ['10sJsQsKsAs',
                 'AsAhAcAd7s',
                 '4H4C7S7D7H',
                 '2H3H4H7HAH',
                 '10HJCQDKSAH',
                 '4H3C7S7D7H',
                 '4H4C7S7DJD',
                 '4H3CASADJD',
                 '4H3C6S5DAD',
                 ]

        for i in range(len(hands)):
            for j in range(i + 1, len(hands)):
                h1 = PokerHand.from_string(hands[i])
                h2 = PokerHand.from_string(hands[j])
                self.assertTrue(h1 > h2, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertFalse(h1 < h2, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertTrue(h2 < h1, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertFalse(h2 > h1, msg='{0}, {1}'.format(hands[i], hands[j]))

    def test_order(self):
        # Hands ordered from best to worst
        hands = ['10sJsQsKsAs', '3c4c5c6c7c', '2H3H4H5HAH',
                 'AsAhAcAd7s', 'AsAhAcAd4s', 'JsJhJcJd4s',
                 '4H4C7S7D7H', '4H4C7S7D4D', '4H4C6S6D4D',
                 '2H3H4H7HAH',
                 '10HJCQDKSAH', '2H3C4D5S6H', '2H3C4D5SAH',
                 '4H3C7S7D7H', '4H4C7S6D4D', '4H4C4S3D2D',
                 '4H4C7S7DJD', '3H3C7S7DJD', '4H4C6S6DJD', '4H4C6S6D5D',
                 '4H3CASADJD', '4H3C7S7DJD', '4H3C5S5DJD', '4H3C5S5D9D',
                 '4H3C6S5DAD', '4H3C6S5DJD'
                 ]

        for i in range(len(hands)):
            for j in range(i + 1, len(hands)):
                h1 = PokerHand.from_string(hands[i])
                h2 = PokerHand.from_string(hands[j])
                self.assertTrue(h1 > h2, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertFalse(h1 < h2, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertTrue(h2 < h1, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertFalse(h2 > h1, msg='{0}, {1}'.format(hands[i], hands[j]))

    def test_order_equal(self):
        hands = [
            ('3c4c5c6c7c', '3d4d5d6d7d'),
            ('2H3H4H7HAH', '4d6d7d9dQd'),
            ('2H3C4D5S6H', '2d3h4c5h6s'),
            ('4H4C7S7DJD', '4d4s7c7hJs'),
            ('4H3CAcAhJD', '4H3CASADJD')
        ]
        for t1, t2 in hands:
            h1 = PokerHand.from_string(t1)
            h2 = PokerHand.from_string(t2)
            self.assertFalse(h1 < h2, msg='{0}, {1}'.format(h1, h2))
            self.assertFalse(h1 > h2, msg='{0}, {1}'.format(h1, h2))
            self.assertFalse(h2 < h1, msg='{0}, {1}'.format(h1, h2))
            self.assertFalse(h2 > h1, msg='{0}, {1}'.format(h1, h2))
