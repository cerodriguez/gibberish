FILES = {
    'words': 'dict/en_GB/words',
    'fruits': 'dict/en_GB/fruits',
    'veggies': 'dict/en_GB/veggies',
    'cheeses': 'dict/en_GB/cheeses'
}


def get_dict(dist):
    _ = []
    with open(dist, 'r') as reader:
        for line in reader:
            line = line.strip()
            _.append(line)
    return _


collection_words = get_dict(FILES['words'])
collection_fruits = get_dict(FILES['fruits'])
collection_veggies = get_dict(FILES['veggies'])
collection_cheeses = get_dict(FILES['cheeses'])
