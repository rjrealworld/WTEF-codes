def mathematical_latex(general_latex):
    general_latex = '+' + general_latex.strip('$').replace(' ', '') + '+'
    reverse_term = ''
    latex_expression = ''
    for element in general_latex[::-1]:
        reverse_term += element
        if element in ['+', '-']:
            latex_expression += reverse_term[::-1]
            reverse_term = ''
    return ('$' + latex_expression.strip('+')+ '$')

#general_latex='$-3x^4-7x^3+21x+17$'
#general_latex='$3x^4-7x^3-21x-17$'
#general_latex='$3x^4-7x^3+21x+17$'
#general_latex='$-3x^4-7x^3-21x-17$'
general_latex='$3x^ 4+  7x^ 3+21x+17$'
print(mathematical_latex(general_latex))