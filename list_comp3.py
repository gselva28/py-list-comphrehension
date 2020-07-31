temp = [99, 'no data', 95, 94, 'no data']
def tech(temp):
    return [i for i in temp if not isinstance(i, str)]