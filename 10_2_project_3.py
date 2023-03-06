def mul(*values):
    output=1
    for num in values:
        if num <10: 
            output*=num
        else:
            pass
    return output

mul(2,3,4,5)
mul(3,12,10)

