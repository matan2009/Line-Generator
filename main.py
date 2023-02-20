from matplotlib.pyplot import plot, show


def get_input_coordinates() -> (int, int, int, int):
    while True:
        try:
            first_coordinate = input("please insert first point coordinates x1, y1: ")
            x1, y1 = map(int, first_coordinate.split(","))
            second_coordinate = input("please insert second point coordinates x2, y2: ")
            x2, y2 = map(int, second_coordinate.split(","))
            return x1, y1, x2, y2

        except ValueError:
            print("Invalid input. Please try again.")


def calculate_line_coordinates(x1: int, y1: int, x2: int, y2: int):
    # Init variables
    x_step, y_step = 0, 0
    x, y = x1, y1

    # Calculate the distance between the two points
    delta_x = x2 - x1
    delta_y = y2 - y1
    abs_delta_x = abs(delta_x)
    abs_delta_y = abs(delta_y)

    steps = max(abs_delta_x, abs_delta_y)
    if steps:
        # Direction to move in x-axis and y-axis
        x_step = delta_x / steps
        y_step = delta_y / steps

    # Store the coordinates in lists
    x_coordinates, y_coordinates = [x], [y]
    line_coordinates = [(x, y)]

    step_num = 0
    # Loop until all steps are done
    while step_num < steps:
        x += x_step
        y += y_step
        x_coordinates.append(x)
        y_coordinates.append(y)
        line_coordinates.append((round(x), round(y)))
        step_num += 1

    # Print line coordinates
    print(line_coordinates)

    # Plot line coordinates
    plot(x_coordinates, y_coordinates, 'bo')
    plot(x_coordinates, y_coordinates, '-')
    show()


def main():
    x1, y1, x2, y2 = get_input_coordinates()
    calculate_line_coordinates(x1, y1, x2, y2)


if __name__ == '__main__':
    main()

