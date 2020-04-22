import http.client
import mimetypes
conn = http.client.HTTPSConnection("localhost", 5555)
payload = ''
headers = {}
conn.request("GET", "/server/entities/data/students", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))