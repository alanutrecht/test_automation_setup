import randomize_deck

from sort_deck import sort_deck, bubbleSort

randomized_deck = randomize_deck.shuffled_deck

new_deck = randomize_deck.card_deck

# sorted_deck = sort_deck(randomized_deck, new_deck)

symbol_sorted_deck = sort_deck(randomized_deck, new_deck)

sorted_deck = bubbleSort(symbol_sorted_deck, new_deck)

# print(symbol_sorted_deck)

print("sorting done!")