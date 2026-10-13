import json

good_text = '{"name": "Leanne Graham"}'
data = json.loads(good_text)
print(data["name"])

bad_text = "Internal Server Error"
data = json.loads(bad_text)
print("Reached the last line")