
if __name__ == "__main__":
    first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
    second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
    first_result = [len(str) for str in first_strings if len(str) > 5]
    second_result = [(str_f, str_s) for str_f in first_strings for str_s in second_strings if len(str_f) == len(str_s)]
    general_list = first_strings + second_strings
    third_result = {gen_l: len(gen_l) for gen_l in general_list if len(gen_l) % 2 == 0}
    print(first_result)
    print(second_result)
    print(third_result)