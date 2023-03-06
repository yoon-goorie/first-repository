def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output+=flatten(item)
        else:
            output.append(item)
    return output
a = [[1, 2], 3, [[4, 5, 6], 7], 8, 9]
flatten(a)