# Island Perimeter
`Algorithm`
`Python`

## Tasks
+ 0. **Island Perimeter**

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

- grid is a list of list of integers:
    - 0 represents water
    - 1 represents land
    - Each cell is square, with a side length of 1
    - Cells are connected horizontally/vertically (not diagonally).
    - grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

### Solution Explanation
The function loops through the grid and checks each cell that represents land. For each land cell, it checks the adjacent cells to determine whether there is water, and adds 1 to the perimeter for each adjacent water cell.

The function then returns the total perimeter of the island.

For example, in the given grid in the testing code sample, there are 12 land cells, and each land cell has two adjacent water cells (except for the four corner cells, which have one adjacent water cell). Therefore, the total perimeter of the island is 12 * 2 + 4 = 28.
