def same_by(characteristic, objects):
    if objects == list():
        return True
    else:
        for i in objects:
            if characteristic(i) != characteristic(objects[1]):
                return False
        return True

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')