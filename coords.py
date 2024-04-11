def coords(x,y):
    if x > 0 and y > 0:
        return 'I'
    if x < 0 and y < 0:
        return 'III'
    if x < 0 and y > 0:
        return 'II'
    if x > 0 and y < 0:
        return 'IV'
    else:
        return 'ZERO'

print(coords(x=int(input('x = ')), y=int(input('y = '))))