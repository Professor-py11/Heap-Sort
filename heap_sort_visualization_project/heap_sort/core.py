import time
import tracemalloc
import sys

#Функція для підтримки властивості max-heap
def heapify(arr, n, i, frames):
    largest = i                        # Нехай i — індекс найбільшого елемента - поточний батьківський вузол (root)
    left = 2 * i + 1                   # Індекс лівого дочірнього вузла
    right = 2 * i + 2                  # Індекс правого дочірнього вузла

    # Якщо лівий дочірній вузол існує і більший за батька
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Якщо правий дочірній вузол існує і більший за поточного найбільшого
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Якщо найбільший елемент — не батько, міняємо місцями
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        frames.append(arr.copy())     # Зберігаємо проміжний стан
        heapify(arr, n, largest, frames)  # Рекурсивно heapify далі


# Основна функція heap sort з візуалізацією
def heap_sort_with_visualization(arr):
    n = len(arr)
    frames = [arr.copy()]  # Зберігаємо початковий стан

    # Початок вимірювання часу з високою точністю
    tracemalloc.start()
    start_time = time.perf_counter()

    # Побудова max-heap (перетворюємо список у купу)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, frames)

    # Один за одним витягуємо елементи з heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Переміщаємо корінь у кінець
        frames.append(arr.copy())       # Зберігаємо стан після swap
        heapify(arr, i, 0, frames)      # Heapify зменшеного heap

    # Кінець вимірювання часу
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    duration = end_time - start_time

    return frames, arr, duration, peak  # Повертаємо пікове використання памʼяті