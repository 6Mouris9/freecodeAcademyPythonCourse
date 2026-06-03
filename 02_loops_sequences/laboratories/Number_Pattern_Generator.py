def number_pattern(n):
    # valida tipo
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    # valida valor
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    # gera padrão
    result = ""
    for i in range(1, n + 1):
        result += str(i)
        if i < n:
            result += " "
    
    return result

print(number_pattern(4))   # "1 2 3 4"
print(number_pattern(1))   # "1"
print(number_pattern(0))   # erro
print(number_pattern("4")) # erro