def is_armstrong(num: int) -> bool:
    as_str = str(num)
    return num == sum(int(ch)**len(as_str) for ch in as_str)
