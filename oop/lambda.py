def format_number(number, function_lambda):
    return function_lambda(number)


currency = format_number(2, lambda x: f"${x}")
decimal = format_number(2, lambda x: f"{x}.00")

print(currency)
print(decimal)
