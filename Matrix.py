class Matrix:

    # Step 1: Create the matrix
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    # Step 2: Print it nicely
    def __str__(self):
        result = ""
        for row in self.data:
            result += str(row) + "\n"
        return result

    # Step 3: Add two matrices
    def __add__(self, other):
        answer = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            answer.append(row)
        return Matrix(answer)

    # Step 4: Subtract two matrices
    def __sub__(self, other):
        answer = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - other.data[i][j])
            answer.append(row)
        return Matrix(answer)

    # Step 5: Multiply by a number (scalar)
    def scale(self, number):
        answer = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] * number)
            answer.append(row)
        return Matrix(answer)

    # Step 6: Matrix multiplication
    def __mul__(self, other):
        answer = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
            answer.append(row)
        return Matrix(answer)

    # Step 7: Transpose (flip rows and columns)
    def transpose(self):
        answer = []
        for j in range(self.cols):
            row = []
            for i in range(self.rows):
                row.append(self.data[i][j])
            answer.append(row)
        return Matrix(answer)

    # Step 8: Determinant (only for square matrices)
    def determinant(self):
 
        # Only square matrices have a determinant
        if self.rows != self.cols:
            print("Error: determinant only works for square matrices!")
            return None
 
        return self._det(self.data)
 
    # Helper function used by determinant (calls itself recursively)
    def _det(self, matrix):
        n = len(matrix)
 
        # BASE CASE 1: 1x1 matrix → just return the single element
        if n == 1:
            return matrix[0][0]
 
        # BASE CASE 2: 2x2 matrix → use the simple formula ad - bc
        if n == 2:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[1][0]
            d = matrix[1][1]
            return a * d - b * c
 
        # BIGGER MATRICES: expand along the first row
        # For each element in row 0:
        #   → remove that column and row 0 → you get a smaller matrix
        #   → multiply element by det of smaller matrix
        #   → alternate + and - signs
        total = 0
        for col in range(n):
 
            # Build the smaller matrix by removing row 0 and current col
            smaller = []
            for row in matrix[1:]:              # skip row 0
                new_row = []
                for j in range(n):
                    if j != col:                # skip current column
                        new_row.append(row[j])
                smaller.append(new_row)
 
            # sign alternates: +, -, +, -, ...
            sign = (-1) ** col
 
            total += sign * matrix[0][col] * self._det(smaller)
 
        return total
    
    # Step 9: Check if two matrices are equal
    def __eq__(self, other):
        return self.data == other.data

    # Step 10: Get shape
    def shape(self):
        return (self.rows, self.cols)


# ── TESTING ──────────────────────────────────────

A = Matrix([[1, 2],
            [3, 4]])

B = Matrix([[5, 6],
            [7, 8]])

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("A + B:")
print(A + B)

print("A - B:")
print(A - B)

print("A * 3 (scale):")
print(A.scale(3))

print("A * B (matrix multiply):")
print(A * B)

print("Transpose of A:")
print(A.transpose())

print("Determinant of A:")
print(A.determinant())
print()

print("Shape of A:", A.shape())

print("Is A == B?", A == B)
print("Is A == A?", A == A)