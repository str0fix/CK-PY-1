from random import sample
import string

def get_random_password(n=None) -> str:
    range_ = ''
    for x in range(0, 10):
        range_ = range_+str(x)
    return_ = ''
    if n is None:
        len_ = 8
    else:
        len_ = n
    for x in sample(string.ascii_letters + range_, len_):
        return_ += x
    return return_


print(get_random_password())
