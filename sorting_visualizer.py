import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


def bubble_sort_animation(data):
    n = len(data)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
                yield data


def generate_random_data(size=10):
    return [random.randint(1, 100) for _ in range(size)]


def update_figure(frame, bars):
    for bar, val in zip(bars, frame):
        bar.set_height(val)
    return bars


def visualize_sorting_algorithm(sort_algorithm, data):
    fig, ax = plt.subplots()
    ax.set_title("Sorting Algorithm Visualization")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_xlim(0, len(data))
    ax.set_ylim(0, max(data) + 10)

    bars = ax.bar(range(len(data)), data, color='red')
    ani = animation.FuncAnimation(fig, update_figure, frames=sort_algorithm(
        data), fargs=(bars,), blit=True, repeat=False, cache_frame_data=False)

    plt.show()


if __name__ == "__main__":
    print("Enter que amount of elements to visualize: ")
    elements_amount = int(input())
    data = generate_random_data(elements_amount)
    visualize_sorting_algorithm(bubble_sort_animation, data)
