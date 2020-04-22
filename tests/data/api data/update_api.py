import http.client
import mimetypes
conn = http.client.HTTPSConnection("localhost", 5555)
payload = "{\n\t\"reference\":\"students\",\n\t\"client_data\":{\n\t\t\"id\":1,\n\t\t\"name\":\"dear mr. student two\",\n\t\t\"age\":35,\n\t\t\"address\":\"address of student two\",\n\t\t\"college\":\"college three\"\n\t}\n}"
headers = {
  'Content-Type': 'application/json',
  'Content-Type': 'application/json'
}
conn.request("POST", "/server/entities/update", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))