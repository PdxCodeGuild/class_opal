import requests
import pprint

# payload = {'contents': text }
# evil insults: no limits on how many times it can be called
# response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json', headers= {'Content-Type': 'application/json'})
# insult = response.json()
# print(insult['insult'])

def evil():
    response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json', headers= {'Content-Type': 'application/json'})
    insult = response.json()
    return insult['insult']
print(evil())

# Shakespeare; calls limit 5/hr or 60/day
"""Using evil function as parameter: 
response = requests.get('https://api.funtranslations.com/translate/shakespeare.json', params={'contents': {'text': evil}})----------------> returned "keyError: 'contents'"

payload = {'text': evil}
response = requests.get('https://api.funtranslations.com/translate/shakespeare.json', params=payload) ----------------> returns the error:
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/requests/models.py", line 971, in json
    return complexjson.loads(self.text, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/rcleav/Desktop/PDX_projects/class_opal/code/rachel/JavaScript/JS_Lab07_MiniCapstone/api_test.py", line 26, in <module>
    results = response.json()
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/requests/models.py", line 975, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
"""

##but this works.......
response = requests.get('https://api.funtranslations.com/translate/shakespeare.json', params={'contents': {'text': evil}})
results = response.json()
print(results['contents']['translated'])