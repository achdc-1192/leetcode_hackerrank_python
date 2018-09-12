number = input()

bin_number = "{0:b}".format(number)
rev_binary = bin_number[::-1]
print int(rev_binary,2)