import random
import string


def get_randomized_path(folder: str, name: str):
    characters = string.ascii_letters + string.digits
    rand = ''.join(random.choice(characters) for _ in range(8))
    return folder + '/' + rand + '_' + name
