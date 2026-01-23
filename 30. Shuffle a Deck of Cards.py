# Shuffle a Deck of Cards

import random

cards = list(range(1, 53))   # 52 cards

for i in range(len(cards)-1, 0, -1):
    j = random.randint(0, i)   # random index
    cards[i], cards[j] = cards[j], cards[i]   # swap

print(cards)
