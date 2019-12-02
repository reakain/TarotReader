import random
import pycorpora

class TarotReader(object):
    def __init__(self):
        self.tarot = pycorpora.divination.tarot_interpretations['tarot_interpretations']
        self.spread = 3

    def get_tarot_reading(self):
        tarot_cards = self.get_tarot_cards()
        tarot_reading = "You've found yourself " \
            + self.get_tarot_meaning(tarot_cards[0], bool(random.getrandbits(1))).lower() + ". " \
            + "Now, however, you're " \
            + self.get_tarot_meaning(tarot_cards[1], bool(random.getrandbits(1))).lower() + ". " \
            + "In the future, you're sure to find yourself " \
            + self.get_tarot_meaning(tarot_cards[2], bool(random.getrandbits(1))).lower() + "."

        return tarot_reading

    def get_tarot_meaning(self,tarot_card, up=True):
        if(up):
            text = tarot_card['meanings']['light']
        else:
            text = tarot_card['meanings']['shadow']

        meaning = text[random.randint(0,len(text)-1)]

        return meaning

    def get_tarot_cards(self):
        tarot_cards = []
        tarot_cards.append(random.choice(self.tarot))
        for x in range(self.spread-1):
            tarot_cards.append(self.get_check_list(tarot_cards,self.tarot))

        return tarot_cards

    def get_check_list(self,build_list, full_list):
        new_item = random.choice(full_list)
        while new_item in build_list:
            new_item = random.choice(full_list)
        return new_item

if __name__ == "__main__":
    tarot = TarotReader()
    print(tarot.get_tarot_reading())