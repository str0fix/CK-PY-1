# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

dict_=range(16)
list_compehension = [{'bin': bin(item), 'dec': item,'oct': oct(item), 'hex': hex(item)} for item in dict_]
pprint(list_compehension)