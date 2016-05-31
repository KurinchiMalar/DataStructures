

def construct_map():
    word_list = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'tweleve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    ty_list = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']
    return word_list,ty_list

def spell_out_numbers(number):

    result = []
    word_list, ty_list = construct_map()

    if number < 100:
        if number < 20:
            result.append(word_list[number])
        else:
            result.append(ty_list[number/10]+" "+word_list[number%10])

        return "".join(result)

    hundredth_digit = number / 100
    result.append(word_list[hundredth_digit]+" hundred ")

    two_digit_no = number % 100

    if two_digit_no > 20:

        tenth_digit = two_digit_no / 10
        result.append(ty_list[tenth_digit]+" ")
        unit_digit = two_digit_no % 10
        result.append(word_list[unit_digit])

    else:

        result.append(word_list[two_digit_no] + " ")


    return "".join(result)


def generic_spell_out(number):

    limit = [" million "," thousand ", ""]

    numbers = [int(x.strip()) for x in number.split(',')]
    print numbers

    result = []
    i = 0
    if len(numbers) > 2:

        for num in numbers:
            if num > 0:
                result.append(spell_out_numbers(num)+limit[i])
            i = i + 1

    elif len(numbers) == 2:
        print spell_out_numbers(numbers[0])
        result.append(spell_out_numbers(numbers[0]) + limit[1])
        result.append(spell_out_numbers(numbers[1]))

    else:
        result.append(spell_out_numbers(numbers))

    print "".join(result)

number = "1,070,201"

#number = 10
#spell_out_numbers(number)
generic_spell_out(number)
#111,222,333

#spell_out_numbers(111)+"million"+spell_out_numbers(222)+"thousand"+spell_out_numbers(333)