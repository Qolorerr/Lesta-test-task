def is_even(value: int) -> bool:
    """
    pros:
    В отличие от функции из примера этот вариант использует побитовую функцию AND,
    что на некоторых процессорах будет быстрее

    cons:
    Этот вариант будет менее читабельным, чем вариант с value % 2 == 0
    :param value:
    :return:
    """
    return value & 1 == 0


print("Some tests:")
print("############")
print("Is even:")
for numb in [10, 17, 20000001, -5, 0]:
    print(f"{numb} {is_even(numb)}")
