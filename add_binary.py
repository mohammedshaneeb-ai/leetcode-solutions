def add_binary(a, b):
    carry = 0
    result = ''
    i = len(a) - 1

    while i >= 0 or carry:
        bit_sum = carry

        if i >= 0:
            bit_sum += int(a[i])
            i -= 1

        if i >= 0:
            bit_sum += int(b[i])
            i -= 1

        carry, bit_sum = divmod(bit_sum, 2)
        result = str(bit_sum) + result

    return result
3


a = '1011'
b = '1010'
print(add_binary(a, b))
