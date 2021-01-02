import hashlib

def gen (paths: str):
    with open(paths, 'rb') as file:
        for line in file.readlines():
            hash_object = hashlib.md5(line)
            yield hash_object.hexdigest()

file_obj = gen('')
for lines in file_obj:
    print(lines)



