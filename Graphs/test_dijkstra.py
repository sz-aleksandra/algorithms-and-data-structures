from dijkstra import read_from_text_file, find_start_and_end_positions, prepare_path, dijkstra_algorithm


def test_1():
    matrix = read_from_text_file("file1.txt")
    start, end = find_start_and_end_positions(matrix)
    path = prepare_path(dijkstra_algorithm(matrix, start, end), start, end)
    assert path == [(1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 4),
                    (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (4, 2)]


def test_2():
    matrix = read_from_text_file("file2.txt")
    start, end = find_start_and_end_positions(matrix)
    path = prepare_path(dijkstra_algorithm(matrix, start, end), start, end)
    assert path == [(0, 19), (1, 19), (2, 19), (3, 19), (4, 19), (5, 19),
                    (5, 18), (6, 18), (7, 18), (8, 18), (9, 18), (9, 17),
                    (9, 16), (9, 15), (9, 14), (9, 13), (9, 12), (9, 11),
                    (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (8, 5),
                    (8, 4), (7, 4), (7, 3), (6, 3), (5, 3), (4, 3), (3, 3)]


def test_3():
    matrix = read_from_text_file("file3.txt")
    start, end = find_start_and_end_positions(matrix)
    path = prepare_path(dijkstra_algorithm(matrix, start, end), start, end)
    assert path == [(0, 27), (1, 27), (2, 27), (2, 26), (2, 25), (2, 24),
                    (3, 24), (4, 24), (5, 24), (6, 24), (7, 24), (8, 24),
                    (9, 24), (9, 23), (9, 22), (9, 21), (9, 20)]


def test_4():
    matrix = read_from_text_file("file4.txt")
    start, end = find_start_and_end_positions(matrix)
    path = prepare_path(dijkstra_algorithm(matrix, start, end), start, end)
    assert path == [(0, 19), (1, 19), (1, 18), (2, 18), (2, 17), (2, 16),
                    (2, 15), (1, 15), (1, 14), (1, 13), (1, 12), (1, 11),
                    (1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4),
                    (1, 3), (1, 2), (1, 1), (1, 0)]
