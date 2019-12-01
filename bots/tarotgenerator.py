import random
import pycorpora

tarot = pycorpora.divination.tarot_interpretations['tarot_interpretations']

spread = 3

def get_tarot_reading():
    tarot_cards = get_tarot_cards()
    tarot_reading = "You've found yourself " \
        + get_tarot_meaning(tarot_cards[0], bool(random.getrandbits(1))).lower() + ". " \
        + "Now, however, you're " \
        + get_tarot_meaning(tarot_cards[1], bool(random.getrandbits(1))).lower() + ". " \
        + "In the future, you're sure to find yourself " \
        + get_tarot_meaning(tarot_cards[2], bool(random.getrandbits(1))).lower() + "."

    return tarot_reading

def get_tarot_meaning(tarot_card, up=True):
    if(up):
        text = tarot_card['meanings']['light']
    else:
        text = tarot_card['meanings']['shadow']

    meaning = text[random.randint(0,len(text)-1)]

    return meaning



def get_tarot_cards():
    tarot_cards = []
    tarot_cards.append(random.choice(tarot))
    for x in range(spread-1):
        tarot_cards.append(get_check_list(tarot_cards,tarot))

    return tarot_cards
    


def get_check_list(build_list, full_list):
    new_item = random.choice(full_list)
    while new_item in build_list:
        new_item = random.choice(full_list)
    return new_item

if __name__ == "__main__":
    print(get_tarot_reading())