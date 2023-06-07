#1.
#unknown = '\u2653'
#print(unknown)
## https://unicode-table.com/en/2653/

#2.
#unknown2 = '\U000057A6'
#print(unknown2)
## https://unicode-table.com/en/57A6/

#3.
#unknown_bytes = unknown.encode('utf-8')
#print(unknown_bytes)
#print(type(unknown_bytes))

#4.
#unknown_string = unknown_bytes.decode('UTF-8')
#print(unknown_string)

#5.
#x = ['hungry', 'in a good mood', 'looking forward to it', 'worried', 'thirsty']
#for i in x:
#    print("I'm {0:s}".format(i))

#6.
import re
letter = """
    Dear Mr. {addressee}:
With reference to our telephone conversation today, 
I am writing to confirm your order for: {amount} x {product} (Ref. No. 856).
Please contact us again if we can help in any way.

Yours sincerely,
{sender}
{post} of {institution}
"""
dict2 = {'addressee':'Addr 234, 23', 'amount': 3, 'product':'Dust', \
'sender':'SendEr', 'post':12321, 'institution':'BergInst'}

#print(letter.format(addressee=dict2.get('addressee'), \
#    amount=dict2.get('amount'), \
#    product=dict2.get('product'), sender=dict2.get('sender'), \
#    post=dict2.get('post'), institution=dict2.get('institution')))
#print(dict2)
for i in dict2:
    letter = re.sub(i, str(dict2.get(i)), letter)

letter = re.sub('{', '', letter)
letter = re.sub('}', '', letter)
print(letter)
    

