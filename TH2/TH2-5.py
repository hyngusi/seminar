import numpy as np

def hungarian_algorithm(cost_matrix):
    num_rows, num_cols = cost_matrix.shape
    label_row = np.zeros(num_rows, dtype=int)
    label_col = np.zeros(num_cols, dtype=int)

    # Step 1: Subtract the minimum value in each row from all elements in that row
    for i in range(num_rows):
        min_value = np.min(cost_matrix[i])
        cost_matrix[i] -= min_value
        label_row[i] += min_value

    # Step 2: Subtract the minimum value in each column from all elements in that column
    for j in range(num_cols):
        min_value = np.min(cost_matrix[:, j])
        cost_matrix[:, j] -= min_value
        label_col[j] += min_value

    mask_matrix = np.zeros_like(cost_matrix, dtype=bool)
    row_covered = np.zeros(num_rows, dtype=bool)
    col_covered = np.zeros(num_cols, dtype=bool)

    # Step 3: Initialize rows and columns as not covered
    rows_covered = 0
    cols_covered = 0

    # Step 4: Find the minimum number of lines to cover all zeros in the matrix
    while rows_covered < num_rows:
        zeros = np.where(cost_matrix == 0)
        row, col = zeros[0][0], zeros[1][0]
        if not row_covered[row] and not col_covered[col]:
            mask_matrix[row, col] = True
            row_covered[row] = True
            col_covered[col] = True
            rows_covered += 1

        if rows_covered < num_rows:
            min_val = np.min(cost_matrix[~row_covered, :][:, ~col_covered])
            cost_matrix[~row_covered, :] -= min_val
            cost_matrix[:, ~col_covered] -= min_val

            for i in range(num_rows):
                for j in range(num_cols):
                    if not row_covered[i] and not col_covered[j]:
                        cost_matrix[i, j] -= min_val
                    elif row_covered[i] and col_covered[j]:
                        cost_matrix[i, j] += min_val

    # Step 5: Construct the assignment
    assignment = []
    for i in range(num_rows):
        for j in range(num_cols):
            if mask_matrix[i, j]:
                assignment.append((i, j))

    return assignment

# Ma trận trọng số
cost_matrix = np.array([
    [4, 9, 5, 1, 4, 9],
    [3, 1, 3, 7, 8, 6],
    [5, 7, 3, 4, 1, 9],
    [8, 8, 3, 7, 6, 6],
    [5, 4, 3, 8, 9, 7],
    [6, 3, 1, 4, 2, 5]
])

assignment = hungarian_algorithm(cost_matrix)
total_cost = sum(cost_matrix[i][j] for i, j in assignment)

print("Assignment:")
for i, j in assignment:
    print(f"Row {i} -> Column {j}")

print("Total Cost:", total_cost)
