"""
cup = '\u2615'
print(len(cup))

result = cup.encode('utf-8')
print(len(result))
print(result)
"""
"""
placement = 'r\u00E9sum\u00E9'
print(placement)
placement_bytes = placement.encode('utf-8')
print(placement_bytes)
print(len(placement_bytes))
print(type(placement_bytes))

other_placement = placement_bytes.decode('utf-8')
print(other_placement)
"""
"""
import string, re
typing_characters = string.printable
print(len(typing_characters))
print(repr(typing_characters[:50]))
print(repr(typing_characters[50:]))
result = re.findall('\d', typing_characters)
print(result)

search_string = 'email' + '!?,' + '\u00E2' + '\u0103'
result = re.findall('\w', search_string)
print(result)
"""

import struct 
valid_png_header = b'\x89PNG\r\n\x1a\n' 
f = open('c:\\Merck\\Python\\Chapter11\\nasa_logo.png', 'rb') 
data = f.read(30) 
if data[:8] == valid_png_header: 
    width, height = struct.unpack('>LL', data[16:24]) 
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')
f.close()
print(data[16:20])
print(data[20:24])