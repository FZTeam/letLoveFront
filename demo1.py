import json
import demjson

data = '''
{
"name":"fanding",
age:18
}
'''

print(demjson.decode(data))
