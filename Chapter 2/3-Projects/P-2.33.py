# Write a Python program that inputs a polynomial in standard algebraic
#  notation and outputs the first derivative of that polynomial.

# 以下结果来自于DeepSeek
import re


def parse_polynomial(poly_str):
    poly_str = poly_str.replace(' ', '')
    terms = re.findall(r'([+-]?[^+-]+)', poly_str)
    return [t for t in terms if t]


def parse_term(term):
    match = re.match(r"^([+-]?)(\d*)(x?)(?:\^(\d+))?$", term)
    if not match:
        return None

    sign_str, coeff_str, x_str, exp_str = match.groups()
    sign = -1 if sign_str == '-' else 1

    try:
        if x_str:
            coeff = int(coeff_str) * sign if coeff_str else sign
            exponent = int(exp_str) if exp_str else 1
        else:
            coeff = int(coeff_str) * sign
            exponent = 0
    except ValueError:
        return None

    return coeff, exponent


def derive_term(coeff, exponent):
    if exponent == 0:
        return (0, 0)
    return (coeff * exponent, exponent - 1)


def format_term(new_coeff, new_exponent):
    if new_coeff == 0:
        return None

    sign = '+' if new_coeff > 0 else '-'
    abs_coeff = abs(new_coeff)

    if new_exponent == 0:
        return f"{sign}{abs_coeff}"
    if new_exponent == 1:
        return f"{sign}{abs_coeff}x"
    return f"{sign}{abs_coeff}x^{new_exponent}"


def main():
    poly_str = input("输入多项式（例如3x^2+5x-7）: ")
    terms = parse_polynomial(poly_str)

    derivative_terms = []
    for term in terms:
        parsed = parse_term(term)
        if not parsed:
            print(f"无效项: {term}")
            return

        coeff, exponent = parsed
        new_coeff, new_exponent = derive_term(coeff, exponent)

        if formatted := format_term(new_coeff, new_exponent):
            derivative_terms.append(formatted)

    if not derivative_terms:
        print("0")
        return

    # 构建最终结果
    result = []
    for i, term in enumerate(derivative_terms):
        if i == 0:
            result.append(term[1:] if term.startswith('+') else term)
        else:
            result.append(f" {term.replace('+', '+').replace('-', '-')}")

    print(''.join(result))


if __name__ == "__main__":
    main()
