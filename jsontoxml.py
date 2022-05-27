from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

# data = readfromurl("https://coderwall.com/vinitcool76.json")
# print(json2xml.Json2xml(data).to_xml())

# data = readfromstring(
#     '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
# )
# print(json2xml.Json2xml(data).to_xml())


data = readfromjson("litch.json")
print(json2xml.Json2xml(data).to_xml())