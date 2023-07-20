def power_function(base_val: int, power_val: int, divisor_val: int) -> int:
    if power_val == 0:
        return 1
    p = power_function(base_val, power_val // 2, divisor_val)
    if power_val % 2 == 0:
        return (p*p) % divisor_val
    return (p*p*base_val) % divisor_val


if __name__ == "__main__":
    base = int(input("Enter base : "))
    power = int(input("Enter power : "))
    divisor = int(input("Enter divisor : "))
    print(f"The value of {base} ^ {power} % {divisor} is : ", power_function(base, power, divisor))
