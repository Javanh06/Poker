"""
Authors: Alexander Bousman and Javan Hirwa
poker_calc.py
Project 11

This program handles the calculation of poker hands
for both the Jacks or Better and Deuces Wild rulesets
"""

from cards import Card
#Do not change the name of these variables
HAND_VALUES_JACKS = {"four_kind": 50, "fullhouse": 12, "flush": 7, "straight": 5, "three": 3, "two_pair":2, "jacks_pair": 1}
HAND_VALUES_DEUCES = {"four_deuce":4000, "five_kind": 18, "straight_flush":10, "four_kind": 7, "fullhouse": 5, "flush": 3, "straight": 3, "three": 1}

def calc_jacks_hands(hand):
    #Get the ranks of the hands and sort them, probably useful later
    hand.sort()
    ranks = (r1, r2, r3, r4, r5) = [card.rank for card in hand]   
    
    if (r1==r2 and r2==r3 and r3==r4) or (r2==r3 and r3==r4 and r4==r5):
        return (HAND_VALUES_JACKS["four_kind"], "Four of a Kind")
    if (r1==r2 and (r3==r4 and r4==r5)) or ((r1==r2 and r2==r3) and (r4==r5)):
        return (HAND_VALUES_JACKS["fullhouse"], "Full House")
    if (hand[0].suit==hand[1].suit and hand[1].suit==hand[2].suit and hand[2].suit == hand[3].suit and hand[3].suit == hand[4].suit):
        return (HAND_VALUES_JACKS["flush"], "Flush")
    
    if r5 == 1:
        if r1 == 2 or r1 == 10:
            if ((r1 == (r2-1)) and (r2 == (r3-1)) and (r3 == (r4-1))):
                return (HAND_VALUES_JACKS["straight"], "Straight")
    else:
        if (r1 == (r2-1)) and (r2 == (r3-1)) and (r3 == (r4-1)) and (r4 == (r5-1)):
            return (HAND_VALUES_JACKS["straight"], "Straight")
        
    if (r1==r2 and r2==r3) or (r2==r3 and r3==r4) or (r3==r4 and r4==r5):
        return (HAND_VALUES_JACKS["three"], "Three of a Kind")
    if (r1==r2 and r3==r4) or (r2==r3 and r4==r5) or (r1==r2 and r4==r5):
        return (HAND_VALUES_JACKS["two_pair"], "Two Pairs")
    
    count = 0
    for i in range(len(ranks)):
        if ranks[i] >= 11 or ranks[i] == 1:
            count += 1
    if count >= 2:
        if (r1==r2) or (r2==r3) or (r3==r4) or (r4==r5):
            return (HAND_VALUES_JACKS["jacks_pair"], "Jacks Pair")
        
    #Just assume you have nothing then...
    return 0, "Nothing"

def calc_deuces_hands(hand):
    # Get a list of the non-deuces, probably useful later
    non_deuces = [card for card in hand if card.rank != 2]
    deuceCount = 5 - len(non_deuces)

    # Example code for checking whether there are Four Deuces
    if len(non_deuces) <= 1:
        return (HAND_VALUES_DEUCES["four_deuce"], "Four Deuces")
    
    fiveCount = 1
    for i in range(len(non_deuces) - 1):
        if non_deuces[i] == non_deuces[i + 1]:
            fiveCount += 1
    if fiveCount == len(non_deuces):
        return (HAND_VALUES_DEUCES["five_kind"], "Five of a Kind")

    fourCount = 0
    for j in range(len(non_deuces) - 1):
        if non_deuces[0] == non_deuces[j]:
            fourCount += 1
        if fourCount == 4 - deuceCount:
            return (HAND_VALUES_DEUCES["four_kind"], "Four of a Kind")
        
    if deuceCount == 1:
        if (non_deuces[0] == non_deuces[1] and non_deuces[2] == non_deuces[3]):
            return (HAND_VALUES_DEUCES["fullhouse"], "Full House")
    else:
        if (non_deuces[0] == non_deuces[1] and (non_deuces[2] == non_deuces[3] and non_deuces[3] == non_deuces[4])) or \
           ((non_deuces[0] == non_deuces[1] and non_deuces[1] == non_deuces[2]) and (non_deuces[3] == non_deuces[4])):
            return (HAND_VALUES_DEUCES["fullhouse"], "Full House")

    suitCount = 1
    isSFlush = True
    for k in range(len(non_deuces) - 1):
        if non_deuces[k].suit == non_deuces[k + 1].suit:
            suitCount += 1
    if suitCount == len(non_deuces):
        for i in range(len(non_deuces) - 1):
            if (non_deuces[i].rank != non_deuces[i+1].rank - 1) and (non_deuces[i+1].rank - non_deuces[i].rank > 2):
                isSFlush = False
        if isSFlush:
            return (HAND_VALUES_DEUCES["straight_flush"], "Straight Flush")
            
    suitCount = 1
    for k in range(len(non_deuces) - 1):
        if non_deuces[k].suit == non_deuces[k + 1].suit:
            suitCount += 1
    if suitCount == len(non_deuces):
        return (HAND_VALUES_DEUCES["flush"], "Flush")
    
    isStraight = True
    gaps = 0
    if deuceCount > 0:
        for i in range(len(non_deuces) - 1):
            if (non_deuces[i+1].rank - non_deuces[i].rank >= 2):
                gaps += 1
            if ((non_deuces[i].rank != non_deuces[i+1].rank - 1) and (gaps > deuceCount)) or ((non_deuces[i] == non_deuces[i+1])):
                isStraight = False
        if isStraight:
            return (HAND_VALUES_DEUCES["straight"], "Straight")
    else:
        if non_deuces[4].rank == 1:
            if non_deuces[0].rank == 2 or non_deuces[0].rank == 10:
                if ((non_deuces[0].rank == (non_deuces[1].rank - 1)) and 
                    (non_deuces[1].rank == (non_deuces[2].rank - 1)) and 
                    (non_deuces[2].rank == (non_deuces[3].rank - 1))):
                    return (HAND_VALUES_DEUCES["straight"], "Straight")
        else:
            if (non_deuces[0].rank == (non_deuces[1].rank - 1) and 
                non_deuces[1].rank == (non_deuces[2].rank - 1) and 
                non_deuces[2].rank == (non_deuces[3].rank - 1) and 
                non_deuces[3].rank == (non_deuces[4].rank - 1)):
                return (HAND_VALUES_DEUCES["straight"], "Straight")

    if deuceCount == 1:
        if (non_deuces[0]==non_deuces[1]) or (non_deuces[1]==non_deuces[2]) or (non_deuces[2]==non_deuces[3]):
            return (HAND_VALUES_DEUCES["three"], "Three of a Kind")
    elif (non_deuces[0]==non_deuces[1] and non_deuces[1]==non_deuces[2]) or (non_deuces[1]==non_deuces[2] and non_deuces[2]==non_deuces[3]) or (non_deuces[2]==non_deuces[3] and non_deuces[3]==non_deuces[4]):
            return (HAND_VALUES_DEUCES["three"], "Three of a Kind")
    
    #Just assume you have nothing then...
    return 0, "Nothing"

def calc_hand(hand, rules = 'JACKS'):
    if len(hand) != 5:
        raise ValueError("This hand doesn't have 5 cards!")
    
    hand = sorted(hand)

    #Depending on the rules paramemter, either check the hand with the Jacks rules or the Deuces Wild rules
    if rules=="JACKS":
        return calc_jacks_hands(hand)
    elif rules=="DEUCES":
        return calc_deuces_hands(hand)
    else:
        raise ValueError(f"{rules} is not a valid ruleset!")