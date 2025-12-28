from cards import Card
from poker_calc import calc_hand, HAND_VALUES_JACKS, HAND_VALUES_DEUCES

def make_card_from_str(card_str):
    suit_strs = ('S', 'H', 'D', 'C')
    suit_lookup = {x:y for x,y in zip(suit_strs, Card.SUITS)}
    rank_lookup = {str(i):i for i in range(2,11)}
    rank_lookup.update({"J":11, "Q":12, "K":13, "A":1})

    suit = card_str[0]
    rank = card_str[1:]
    if rank not in rank_lookup:
        raise ValueError(f"Card {card_str} has an invalid rank {rank}")
    if suit not in suit_lookup:
        raise ValueError(f"Card {card_str} has an invalid suit {suit}")
    return Card(rank = rank_lookup[rank], suit = suit_lookup[suit])

def make_hand_from_str(hand_str):
    card_strs = hand_str.split()
    if len(card_strs)!=5:
        raise RuntimeError(f"Hand only has {len(card_strs)} cards...")
    else:
        cards = [make_card_from_str(card) for card in card_strs]
        return cards

#Use this test to test hands from input
def input_hand_test(rules = 'JACKS'):
    while True:
        card_str = input("Please type in a hand:")
        if card_str =="":
            break
        cards = string_hand_test(card_str, rules, display_hands = True)

#This runs and returns the score for a hand given as a string
def string_hand_test(card_str, rules = 'JACKS', display_hands = False):
    cards = make_hand_from_str(card_str)
    score, hand = calc_hand(cards, rules = rules)
    cards_as_str = ", ".join((str(card) for card in cards))

    if display_hands:
        print("Calculation result:")
        print(f"Cards: {cards_as_str}")
        print(f"Hand: {hand}")
        print(f"Score: {score}")

    return score

def test_jacks_hands():    
    testHand_four = "S5 H5 D5 C5 D10"
    testHand_fullhouse = "S10 H10 C10 DJ HJ"
    testHand_flush = "S10 S5 S2 SA SK"
    testHand_straight = "S10 HJ DQ HK SA"
    testHand_low_straight = "SA D2 C3 D4 D5"
    testHand_three = "D5 S5 C5 C2 D6"
    testHand_two_pair = "D5 S5 C10 D10 S6"
    testHand_jack_pair = "DK SK C10 D9 S6"
    testHand_jack_pair2 = "DA CA C10 C9 C8"
    testHand_bad1 = "S10 H9 D7 C5 C4"
    testHand_bad2 = "S10 H10 D7 C5 C4"
    testHand_bad3 = "S2 H3 C7 D5 D3"

    print("Testing hands...")
    assert string_hand_test(testHand_four) == HAND_VALUES_JACKS["four_kind"]
    assert string_hand_test(testHand_fullhouse) == HAND_VALUES_JACKS["fullhouse"]
    assert string_hand_test(testHand_flush) == HAND_VALUES_JACKS["flush"]
    assert string_hand_test(testHand_straight) == HAND_VALUES_JACKS["straight"]
    assert string_hand_test(testHand_low_straight) == HAND_VALUES_JACKS["straight"]
    assert string_hand_test(testHand_three) == HAND_VALUES_JACKS["three"]
    assert string_hand_test(testHand_two_pair) == HAND_VALUES_JACKS["two_pair"]
    assert string_hand_test(testHand_jack_pair) == HAND_VALUES_JACKS["jacks_pair"]
    assert string_hand_test(testHand_jack_pair2) == HAND_VALUES_JACKS["jacks_pair"]

    assert string_hand_test(testHand_bad1) == 0
    assert string_hand_test(testHand_bad2) == 0       # Pair is too low
    assert string_hand_test(testHand_bad3) == 0
    print("Successful scores calculated on the test hands.")
    
def test_deuces_hands():    
    testHand_four = "S5 H5 D5 C5 D10"
    testHand_fullhouse = "S10 H10 C10 DJ HJ"
    testHand_flush = "S10 S5 S3 SA SK"
    testHand_straight = "S10 HJ DQ HK SA"
    testHand_low_straight = "SA D2 C3 D4 D5"
    testHand_three = "D5 S5 C5 C3 D6"
    testHand_two_pair = "D5 S5 C10 D10 S6"
    testHand_jack_pair = "DK SK C10 D9 S6"
    testHand_jack_pair2 = "DA CA C10 C9 C8"
    testHand_bad1 = "S10 H9 D7 C5 C4"
    testHand_bad2 = "S10 H10 D7 C5 C4"
    testHand_bad3 = "S6 H3 C7 D5 D3"
    

    print("Testing hands...")
    test_deuce_hand = lambda x: string_hand_test(x, rules="DEUCES")
    assert test_deuce_hand(testHand_four) == HAND_VALUES_DEUCES["four_kind"]
    assert test_deuce_hand(testHand_fullhouse) == HAND_VALUES_DEUCES["fullhouse"]
    assert test_deuce_hand(testHand_flush) == HAND_VALUES_DEUCES["flush"]
    assert test_deuce_hand(testHand_straight) == HAND_VALUES_DEUCES["straight"]
    assert test_deuce_hand(testHand_low_straight) == HAND_VALUES_DEUCES["straight"]
    assert test_deuce_hand(testHand_three) == HAND_VALUES_DEUCES["three"]
    assert test_deuce_hand(testHand_two_pair) == 0
    assert test_deuce_hand(testHand_jack_pair) == 0
    assert test_deuce_hand(testHand_jack_pair2) == 0
    assert test_deuce_hand(testHand_bad1) == 0
    assert test_deuce_hand(testHand_bad2) == 0    
    assert test_deuce_hand(testHand_bad3) == 0

    print("Testing hands with deuces...")
    testHand_four_Deuce = "S2 H2 D2 C2 H8"
    testHand_five = "S5 H5 D5 C5 H2"
    testHand_four = "S5 H5 D5 C2 D10"
    testHand_fullhouse = "S10 H2 C10 DJ HJ"
    testHand_flush = "S10 S5 H2 SA D2"
    testHand_straight_flush = "D10 H2 DQ DK S2"
    testHand_straight = "S10 H2 DQ HK S2"
    testHand_straight2 = "D2 C3 H2 D5 C6"
    testHand_three = "D5 S5 C2 C3 D6"
    testHand_bad1 = "S10 H9 D7 C5 C2"
    testHand_bad2 = "S10 D2 D7 C5 C4"
    
    assert test_deuce_hand(testHand_four_Deuce) == HAND_VALUES_DEUCES["four_deuce"]
    assert test_deuce_hand(testHand_five) == HAND_VALUES_DEUCES["five_kind"]
    assert test_deuce_hand(testHand_four) == HAND_VALUES_DEUCES["four_kind"]
    assert test_deuce_hand(testHand_fullhouse) == HAND_VALUES_DEUCES["fullhouse"]
    assert test_deuce_hand(testHand_flush) == HAND_VALUES_DEUCES["flush"]
    assert test_deuce_hand(testHand_straight_flush) == HAND_VALUES_DEUCES["straight_flush"]
    assert test_deuce_hand(testHand_straight) == HAND_VALUES_DEUCES["straight"]
    assert test_deuce_hand(testHand_straight2) == HAND_VALUES_DEUCES["straight"]
    assert test_deuce_hand(testHand_three) == HAND_VALUES_DEUCES["three"]
    assert test_deuce_hand(testHand_bad1) == 0
    assert test_deuce_hand(testHand_bad2) == 0    
    print("Successful scores calculated on the test hands.")

    score_only = lambda x: calc_hand(x)[0]
if __name__ == "__main__":
    test_jacks_hands()
    test_deuces_hands()

    #Use one of these if you want to test custom hands instead
    #input_hand_test()
    #input_hand_test(rules="DEUCES")
