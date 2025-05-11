import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Функція анімації
def animate_sort(frames):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(frames[0])), frames[0], align="edge", color='skyblue')
    ax.set_title("Heap Sort Visualization")
    ax.set_ylim(0, max(map(max, frames)) * 1.1)  # масштабування

    # Створення текстів над стовпчиками
    texts = [ax.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 0.5, 
                     f'{int(rect.get_height())}', ha='center', va='bottom', fontsize=8)
             for rect in bar_rects]

    def update(frame):
        for rect, height, text in zip(bar_rects, frame, texts):
            rect.set_height(height)
            text.set_y(height + 0.5)
            text.set_text(f'{int(height)}')
        return list(bar_rects) + texts  # <-- перетворено bar_rects на список

    ani = animation.FuncAnimation(fig, update, frames=frames, interval=500, repeat=False)
    plt.show()