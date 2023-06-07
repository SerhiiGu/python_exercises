"""
from collections import OrderedDict
from pprint import pprint
regions = OrderedDict([
    ('mountains', 'Himalayas'),
    ('sands', 'Sahara'),
    ('rivers', 'Yangtze')
])
print(regions)
pprint(regions)
"""

import pprint
print(dir(pprint))

import locale
print(locale.getpreferredencoding())