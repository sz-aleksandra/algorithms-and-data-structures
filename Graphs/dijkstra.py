import heapq
import sys


def read_from_text_file(filepath):
    with open(filepath, "r") as file_handle:
        matrix = [list(map(int, list(line.strip()))) for line in file_handle]
    return matrix


def find_start_and_end_positions(matrix):
    start, end = None, None
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 0:
                if start is None:
                    start = (row, column)
                else:
                    end = (row, column)
                    return start, end


def dijkstra_algorithm(matrix, start, end):
    distances = [[float("inf")] * len(matrix[0]) for _ in range(len(matrix))]
    distances[start[0]][start[1]] = 0
    queue = [(0, start)]
    previous = {}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        (cost, (x, y)) = heapq.heappop(queue)
        if (x, y) == end:
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                ncost = cost + matrix[nx][ny]
                if ncost < distances[nx][ny]:
                    distances[nx][ny] = ncost
                    heapq.heappush(queue, (ncost, (nx, ny)))
                    previous[(nx, ny)] = (x, y)
    return previous


def prepare_path(previous, start, end):
    x, y = end
    path = []
    while (x, y) != start:
        path.append((x, y))
        x, y = previous[(x, y)]
    path.append(start)
    return path[::-1]


def print_result(matrix, path):
    for row in range(len(matrix)):
        print_row = []
        for column in range(len(matrix[0])):
            if (row, column) in path:
                print_row.append(str(matrix[row][column]))
            else:
                print_row.append(" ")
        print("".join(print_row))


def main():
    file = sys.argv[1]
    matrix = read_from_text_file(file)
    start, end = find_start_and_end_positions(matrix)
    path = prepare_path(dijkstra_algorithm(matrix, start, end), start, end)
    print_result(matrix, path)


if __name__ == "__main__":
    main()
