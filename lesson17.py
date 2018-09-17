import json

j = {
    "employee":
        [
            {"id": 100, "name": "Mike"},
            {"id": 101, "name": "Nancy"}
        ]
}

print(j)
print('####################')
print(json.dumps(j))
print('####################')
a = json.dumps(j)
print(json.loads(a))

with open('test.json', 'w') as f:
    # dump's' じゃない
    json.dump(j, f)

with open('test.json', 'r') as f:
    print(json.load(f))

# dumps の s は str 的な意味合いっぽい
# ストリームとして扱うなら、dump でOK