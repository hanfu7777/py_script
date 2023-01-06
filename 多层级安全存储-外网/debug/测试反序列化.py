a = '[1,2,3]'
d = '''{"测试":"韩同学"}'''
import json
print(type(d))
d = json.loads(d)
print(type(d))

