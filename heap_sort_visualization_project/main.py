import random
from heap_sort.core import heap_sort_with_visualization
from heap_sort.visualizer import animate_sort

if __name__ == "__main__":
    arr = random.sample(range(1, 30), 10)
    print("Original array:", arr)
    frames, sorted_arr, duration, memory_used = heap_sort_with_visualization(arr.copy())
    print("Sorted array:  ", sorted_arr)
    print(f"\n⏱ Час виконання: {duration:.4f} секунд")
    print(f"📦 Памʼять для frames: {memory_used / 1024:.2f} KB")
    print("\n🧠 Теоретична складність:")
    print("   - Часова: O(n log n)")
    print("   - Просторова: O(1) для сортування, O(k * n) для візуалізації")
    animate_sort(frames)