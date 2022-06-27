import yaml
import cbor2 as cbor
from pprint import pprint

with open('./data.yaml', 'r') as file:
    data = yaml.load(file)

print(type(data))
as_cbor = cbor.dumps(data)
print(type(as_cbor))
print(as_cbor)
for c in as_cbor:
    print(f'{c:02x} ', end='')
print()
# pprint(data)
# print()

# out_data = []
# for i in range(4):
#     out_data.append({'count': i})

# print(yaml.dump(out_data))