#!/usr/bin/python3

import unittest

from Card import *
from Poker import *


class PokerTests7(unittest.TestCase):
    def test_is_straight7(self):
        self.assertTrue(PokerHand.from_string('2H3C4D5S6HJC8D').is_straight())
        self.assertFalse(PokerHand.from_string('2H3C4D5S7HJC3D').is_straight())
        self.assertTrue(PokerHand.from_string('2H3C4D5SAHJC3D').is_straight())
        self.assertTrue(PokerHand.from_string('2H3H4H5HAHJC3D').is_straight())
        self.assertTrue(PokerHand.from_string('10HJCQDKSAHJC3D').is_straight())

    def test_is_flush7(self):
        self.assertTrue(PokerHand.from_string('2H3H4H5HAHJC8D').is_flush())
        self.assertTrue(PokerHand.from_string('2H3H4H7HAHJC8D').is_flush())
        self.assertFalse(PokerHand.from_string('2H3H4S5HASJC8D').is_flush())
        self.assertFalse(PokerHand.from_string('2H3H4S5HAHJC8D').is_flush())

    def test_is_straight_flush7(self):
        self.assertTrue(PokerHand.from_string('2H3H4H5HAHJC8D').is_straight_flush())
        self.assertFalse(PokerHand.from_string('2H3H4H5H7HJC8D').is_straight_flush())
        self.assertFalse(PokerHand.from_string('2H3C4D5S6HJC8D').is_straight_flush())
        self.assertFalse(PokerHand.from_string('2C3C4D5S6CJC8C').is_straight_flush())

    def test_get_kinds7(self):
        hand = PokerHand.from_string('4H4C7S7DJD5H6D')
        kinds = hand.get_kinds()
        self.assertEqual({Rank.Four: 2, Rank.Seven: 2, Rank.Five:1, Rank.Six:1, Rank.Jack: 1}, kinds)

    def test_is_full_house7(self):
        self.assertFalse(PokerHand.from_string('4H4C7S7DJDJC8C').is_full_house())
        self.assertTrue(PokerHand.from_string('4H4C7S7D4DJC8C').is_full_house())

    def test_is_two_pair7(self):
        self.assertTrue(PokerHand.from_string('4H4C7S7DJDJC8C').is_two_pair())
        self.assertFalse(PokerHand.from_string('4H4C7S7D4DJC8C').is_two_pair())

    def test_order_simple7(self):
        # Hands ordered from best to worst
        hands = ['10sJsQsKsAsJC8C',
                 'AsAhAcAd7sJC8C',
                 '4H4C7S7D7HJC8C',
                 '2H3H4H7HAHJC8C',
                 '10HJCQDKSAHJD8C',
                 '4H3C7S7D7HJD8C',
                 '4H4C7S7DJD6D8C',
                 '4H3CASADJD6D8C',
                 '4H3C6S5DADJD8C',
                 ]

        for i in range(len(hands)):
            for j in range(i + 1, len(hands)):
                h1 = PokerHand.from_string(hands[i])
                h2 = PokerHand.from_string(hands[j])
                self.assertTrue(h1 > h2, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertFalse(h1 < h2, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertTrue(h2 < h1, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertFalse(h2 > h1, msg='{0}, {1}'.format(hands[i], hands[j]))

    def test_order7(self):
        # Hands ordered from best to worst
        hands = ['10sJsQsKsAs7d4d', '3c4c5c6c7c7d4d', '2H3H4H5HAH7d4d',
                 'AsAhAcAd7s7d4d', 'AsAhAcAd4s5s3h', 'JsJhJcJd4s7d4d',
                 '4H4C7S7D7H5c3c', '4H4C7S7D4D5c3c', '4H4C6S6D4D5c3c',
                 '2H3H4H7HAH6c3c',
                 '10HJCQDKSAH6c3c', '2H3C4D5S6H6c3c', '2H3C4D5SAH7c3c',
                 '4H3C7S7D7H6c2c', '4H4C7S6D4DKc8c', '4H4C4S3D2DQc8c',
                 '4H4C7S7DJD6c2c', '3H3C7S7DJD6c2c', '4H4C6S6DJD5c2c', '4H4C6S6D5D7c2c',
                 '4H3CASADJD8c6c', '4H3C7S7DJD8c6c', '4H3C5S5DJD8c6c', '4H3C5S5D9D8c6c',
                 '4H3C6S5DAD8c9c', '4H3C6S5DJD8c9c'
                 ]

        for i in range(len(hands)):
            for j in range(i + 1, len(hands)):
                h1 = PokerHand.from_string(hands[i])
                h2 = PokerHand.from_string(hands[j])
                self.assertTrue(h1 > h2, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertFalse(h1 < h2, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertTrue(h2 < h1, msg='{0}, {1}'.format(hands[i], hands[j]))
                self.assertFalse(h2 > h1, msg='{0}, {1}'.format(hands[i], hands[j]))

    def test_order_equal7(self):
        hands = [
            ('3c4c5c6c7c9sJs', '3d4d5d6d7dQsKs'),
            ('2H3H4H7HAH9sJs', '4d6d7d9dQdQsKs'),
            ('2H3C4D5S6H9sJs', '2d3h4c5h6sQsKs'),
            ('4H4C7S7DJD3s6s', '4d4s7c7hJs2s5s'),
            ('8HQCAcAhJD3s6s', '8HQCASADJD2s5s')
        ]
        for t1, t2 in hands:
            h1 = PokerHand.from_string(t1)
            h2 = PokerHand.from_string(t2)
            self.assertFalse(h1 < h2, msg='{0}, {1}'.format(h1, h2))
            self.assertFalse(h1 > h2, msg='{0}, {1}'.format(h1, h2))
            self.assertFalse(h2 < h1, msg='{0}, {1}'.format(h1, h2))
            self.assertFalse(h2 > h1, msg='{0}, {1}'.format(h1, h2))
