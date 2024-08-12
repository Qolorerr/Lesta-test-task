from collections import deque
from typing import Any


class FIFOlist:
    """
    Эта реализация основана на list

    pros:
    Есть возможность получения доступа к элементам по индексу

    cons:
    Память выделяется при инициализации, потому при малой заполненности
    низкая эффективность использования памяти
    """
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size
        self.start = 0
        self.end = 0
        # Flag to avoid pop from empty list
        self.is_full = False

    def add(self, value: Any) -> None:
        self.data[self.end] = value
        if self.is_full:
            self.start = (self.start + 1) % self.size
        self.end = (self.end + 1) % self.size
        self.is_full = self.end == self.start

    def pop(self) -> Any:
        if not self.is_full and self.start == self.end:
            raise IndexError("Buffer is empty")
        value = self.data[self.start]
        self.data[self.start] = None
        self.start = (self.start + 1) % self.size
        self.is_full = False
        return value

    def __str__(self) -> str:
        if self.start < self.end:
            return str(self.data[self.start:self.end])
        if self.start > self.end or self.is_full:
            return str(self.data[self.start:] + self.data[:self.end])
        return "[]"

    def __getitem__(self, index) -> Any:
        return self.data[(self.start + index) % self.size]


class FIFOlist_simple:
    """
    Эта реализация также основана на list

    pros:
    Очень простой и читабельный код. Не требует знания библиотек.
    Также есть доступ к элементам по индексу

    cons:
    Плохая эффективность по времени при добавлении и удалении элемента
    """
    def __init__(self, size: int):
        self.size = size
        self.data = []

    def add(self, value: Any) -> None:
        self.data.append(value)
        if len(self.data) > self.size:
            self.data.pop(0)

    def pop(self) -> Any:
        return self.data.pop(0)

    def __str__(self) -> str:
        return str(self.data)

    def __getitem__(self, index) -> Any:
        return self.data[index]


class FIFOdeque:
    """
    Эта реализация также основана на deque из библиотеки collections

    pros:
    Высокая скорость добавления и удаления элемента - O(1).
    Также память выделяется по мере заполнения

    cons:
    Нет доступа к элементам по индексу
    """
    def __init__(self, size: int):
        self.size = size
        self.buffer = deque(maxlen=size)

    def add(self, value: Any) -> None:
        self.buffer.append(value)

    def pop(self) -> Any:
        if not self.buffer:
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()

    def __str__(self) -> str:
        return str(list(self.buffer))


print("Some tests:")
print("############")
structures = [FIFOlist, FIFOlist_simple, FIFOdeque]
ARRAY_SIZE = 3
for structure in structures:
    array = structure(ARRAY_SIZE)
    print(type(array).__name__)
    print(array)
    array.add(1)
    array.add(2)
    print(array)
    array.add(3)
    array.add(4)
    print(array)
    print(array.pop())
    print(array)
    print()
