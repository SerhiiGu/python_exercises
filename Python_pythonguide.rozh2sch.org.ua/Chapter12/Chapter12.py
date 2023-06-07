import urllib.request as ur
url = 'http://openweathermap.org'
conn = ur.urlopen(url)
data = conn.read()
print(conn.status)
print(conn.getheader('Content-Type'))
for key, value in conn.getheaders():
    print(key, value)
#print(data)