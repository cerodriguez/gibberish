import random


def word_generator(words, category):
    """
    Simple words generator

    :param words:list
    :param category:list
    :return:str
    """
    while True:
        for word in words:
            cat = random.choice(category)
            name = f'{cat.title()} {word.title()}'
            yield name
