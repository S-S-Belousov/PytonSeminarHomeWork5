from os import path


def get_new_text(text, str='абв'):
    new_text = []
    for i in text.split():
        if i.count(str):
            new_text.append(i)
    return ' '.join(new_text)


def encoding_text(text):
    code_list = []
    text_char = text[0]
    char_count = 0
    for i in range(0, len(text)):
        if text[i] == text_char and i < len(text):
            char_count += 1
        else:
            code_list.append(str(char_count)+text_char)
            char_count = 1
            text_char = text[i]
    code_list.append(str(char_count)+text_char)
    return ''.join(code_list)


def decoding_text(text):
    code_list = []
    char_count = ''
    for i in range(0, len(text)):
        if text[i].isdigit():
            char_count += text[i]
        else:
            code_list.append(text[i]*int(char_count))
            char_count = ''
    return ''.join(code_list)


def encoding_file(filename):
    if (path.exists(filename)):
        with open(filename, 'r') as original_file:
            txt_list_file = original_file.read().splitlines()
            with open('encoding_file.txt', 'w') as encoding_file:
                for i in txt_list_file:
                    encoding_file.write(encoding_text(i)+'\n')
    
        return 'Создан файл "encoding_file.txt"'
    else:
        return 'Файл "' + filename + '" не найден'

def decoding_file(filename):
    if (path.exists(filename)):
        with open(filename, 'r') as encoding_file:
            txt_list_file = encoding_file.read().splitlines()
            with open('decoding_file.txt', 'w') as decoding_file:
                for i in txt_list_file:
                    decoding_file.write(decoding_text(i)+'\n')
        return 'Создан файл "decoding_file.txt"'
    else:
        return 'Файл "' + filename + '" не найден'


def get_prime_factors(factors):
    prime_factors_list = []
    for i in range(2, int(factors)+1):
        counter = 0
        for j in range(2, i):
            if i % j == 0:
                counter += 1
        if counter == 0:
            prime_factors_list.append(i)
    return prime_factors_list


def get_non_repeating_elements(elements_list):
    non_repeating_list = []
    for i in elements_list:
        if elements_list.count(i) == 1:
            non_repeating_list.append(i)
    return non_repeating_list


def get_polynomial(degree, number_of_monomials='3'):
    return {
        number_of_monomials == '1': str(randint(2, 11))+'*X**'+degree+'=0',
        number_of_monomials == '2': str(randint(2, 11))+'*X**'+degree+'+'+str(randint(2, 11))+'*X=0',
        number_of_monomials == '3': str(randint(2, 11))+'*X**'+degree+'+'+str(randint(2, 11))+'*X+'+str(randint(2, 11))+'=0'
    }[True]
