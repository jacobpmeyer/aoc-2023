def camel_cards(input):
    hand_bids = input.split("\n")[1:-1]
    return hand_bids

input1 = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

print(camel_cards(input1))
