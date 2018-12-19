import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def convert_letter_to_num(card):
    card_num = 0
    letter_to_num = {'J':11,'Q':12,'K':13,'A':14}
    card_num_str = card[:-1]
    if card_num_str in letter_to_num.keys():
        card_num = letter_to_num[card_num_str]
    else:
        card_num = int(card_num_str)
    return card_num

def is_bigger(card1, card2):
    card1_num = convert_letter_to_num(card1)
    card2_num = convert_letter_to_num(card2)
    #print("card1_num:{},card2_num:{}".format(card1_num,card2_num), file=sys.stderr)

    if card1_num > card2_num:
        return True
    elif card1_num < card2_num:
        return False
    elif card1_num == card2_num:
        return 'SAME'


def handling_war(cardp1, cardp2, temp1_q=None, temp2_q=None):
    print("handling war", file=sys.stderr)
    if temp1_q is None:
        temp1_q = []
    if temp2_q is None:
        temp2_q = []
    if len(cardp1) > 4 and len(cardp2) > 4:
        temp1_q += cardp1[0:4]
        temp2_q += cardp2[0:4]
        working_card1 = cardp1[4]
        working_card2 = cardp2[4]
        cardp1_num = convert_letter_to_num(working_card1)
        cardp2_num = convert_letter_to_num(working_card2)
        print("temp1_q:{},temp2_q:{}".format(temp1_q, temp2_q), file=sys.stderr)
        print("Comparing cards:{},{}".format(working_card1,working_card2), file=sys.stderr)
        cardp1 = cardp1[4:]
        cardp2 = cardp2[4:]
        if cardp1_num > cardp2_num:
            cardp1 += temp1_q
            cardp1.remove(working_card1)
            cardp1.append(working_card1)
            cardp1 += temp2_q
            cardp1.append(working_card2)
            cardp2.remove(working_card2)
        elif cardp1_num < cardp2_num:
            cardp2 += temp1_q
            cardp1.remove(working_card1)
            cardp2.append(working_card1)
            cardp2 += temp2_q
            cardp2.remove(working_card2)
            cardp2.append(working_card2)
        elif cardp1_num == cardp2_num:
            cardp1, cardp2 = handling_war(cardp1, cardp2, temp1_q, temp2_q)
        return cardp1, cardp2
    else:
        return 'PAT', 'PAT'

#cardp_1 = []
#cardp_2 = []

#n = int(input())  # the number of cards for player 1
#for i in range(n):
#    cardp_1.append(input())  # the n cards of player 1
#m = int(input())  # the number of cards for player 2
#for i in range(m):
#    cardp_2.append(input())  # the m cards of player 2


cardp_1 = ['10H', 'KD', '6C', '10S', '8S', 'AD', 'QS', '3D', '7H', 'KH', '9D', '2D', 'JC', 'KS', '3S', '2S', 'QC', 'AC', 'JH', '7D', 'KC', '10D', '4C', 'AS', '5D', '5S']
cardp_2 = ['2H', '9C', '8C', '4S', '5C', 'AH', 'JD', 'QH', '7C', '5H', '4H', '6H', '6S', 'QD', '9H', '10C', '4D', 'JS', '6D', '3H', '8H', '3C', '7S', '9S', '8D', '2C']


print("cardp_1:{}".format(cardp_1), file=sys.stderr)
print("cardp_2:{}".format(cardp_2), file=sys.stderr)

count = 0
while len(cardp_1) and len(cardp_2):
    print("round:{} comparing:{} and {}".format(count, cardp_1[0], cardp_2[0]), file=sys.stderr)
    bigger = is_bigger(cardp_1[0], cardp_2[0])
    if bigger is True:
        cardp_1.append(cardp_1[0])
        cardp_1.append(cardp_2[0])
        cardp_1.remove(cardp_1[0])
        cardp_2.remove(cardp_2[0])
    elif bigger is False:
        cardp_2.append(cardp_1[0])
        cardp_2.append(cardp_2[0])
        cardp_1.remove(cardp_1[0])
        cardp_2.remove(cardp_2[0])
    elif bigger == 'SAME':
        cardp_1, cardp_2 = handling_war(cardp_1, cardp_2)

    print("cardp_1:{}".format(cardp_1), file=sys.stderr)
    print("cardp_2:{}".format(cardp_2), file=sys.stderr)

    count += 1

    if cardp_1 == 'PAT' or cardp_2 == 'PAT':
        print("PAT")
        break
    elif len(cardp_1) == 0:
        print("2 {}".format(count))
        break
    elif len(cardp_2) == 0:
        print("1 {}".format(count))
        break
