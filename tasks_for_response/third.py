from typing import Iterable, Callable


def sort(array: Iterable, key: Callable | None = None, reverse: bool = False) -> Iterable:
    """
    Я бы использовал базовую сортировку python - timsort.
    Она объединяет в себе достоинства скорости сортировки слиянием на больших списках
    и сортировки вставки на маленьких

    Работает за O(n) в лучшем случае (массив уже отсортирован) и за O(n*logn) в худшем

    На случайных наборах данных эффективнее было бы использовать quicksort, однако на
    прикладных задачах timsort часто оказывается быстрее
    :param array:
    :param key:
    :param reverse:
    :return:
    """
    return sorted(array, key=key, reverse=reverse)
