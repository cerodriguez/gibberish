from generators import word_generator
from dictonaries import collection_words, collection_fruits, collection_veggies, collection_cheeses

fruit_generator = word_generator(collection_words, collection_fruits)
veggies_generator = word_generator(collection_words, collection_veggies)
cheese_generator = word_generator(collection_words, collection_cheeses)


def get_fruit():
    return next(fruit_generator)


def get_veggie():
    return next(veggies_generator)


def get_cheese():
    return next(cheese_generator)
