numbers = '010-12345-23456'
def change_num(nums):
    answer = numbers.replace(numbers[-5:],'#####')
    return answer
change_num('010-12345-23456')
