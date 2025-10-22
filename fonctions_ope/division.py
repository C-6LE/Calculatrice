def division(*args:int) -> int:
    sum_number: int = args[0]

    for i in args[1:]:
        sum_number /= i

    return sum_number
