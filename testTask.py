def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
    
max_number: int = None
max_digit_sum: int = -1

while True:
    user_input = input("Введите целое число (0 для выхода): ")

    if user_input == "0":
        break
    
    try:
        current_number = int(user_input)
        if current_number < 0:
            raise ValueError("Пожалуйста, введите положительное целое число.")
        
        current_digit_sum = sum_of_digits(current_number)
        
        if current_digit_sum > max_digit_sum:
            max_digit_sum = current_digit_sum
            max_number = current_number

    except ValueError as e:
        print(f"Ошибка: {e}. Пожалуйста, попробуйте снова.")

if max_number is not None:
    print(f"Число с максимальной суммой цифр: {max_number} (Сумма цифр: {max_digit_sum})")
else:
    print("Не было введено ни одного числа.")