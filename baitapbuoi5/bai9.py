def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(min(len(input_tuple), len(input_tuple[0]))))

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

output_tuple = get_diagonal(input_tuple)
print(output_tuple)
