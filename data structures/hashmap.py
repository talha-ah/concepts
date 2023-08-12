hashmap = {}
hashmap["a"] = 1
hashmap["b"] = 2
hashmap["c"] = 3
hashmap["d"] = 5

print(hashmap)

del hashmap["a"]

print(hashmap)

for key in hashmap:
    print(key, hashmap[key])

print("a" in hashmap)
print("b" in hashmap)
