class Solution {
    void bfs(vector<vector<int>>& grid, int row, int col) {
        if (grid[row][col])
            return;

        queue<pair<int, int>> q;

        q.push(make_pair(row, col));

        while (!q.empty()) {
            pair<int, int> curr = q.front();
            q.pop();

            int dist = grid[curr.first][curr.second] + 1;
            // cout << "processing " << curr.first << ", " << curr.second << ", dist: " << dist << endl;

            int currRow = curr.first + 1;
            int currCol = curr.second;

            if (currRow < grid.size() && grid[currRow][currCol] > dist) {
                grid[currRow][currCol] = dist;
                q.push(make_pair(currRow, currCol));
            }

            currRow = curr.first - 1;

            if (currRow >= 0 && grid[currRow][currCol] > dist) {
                grid[currRow][currCol] = dist;
                q.push(make_pair(currRow, currCol));
            }

            currRow = curr.first;
            currCol = curr.second - 1;

            if (col >= 0 && grid[currRow][currCol] > dist) {
                grid[currRow][currCol] = dist;
                q.push(make_pair(currRow, currCol));
            }

            currCol = curr.second + 1;
            if (currCol < grid[0].size() && grid[currRow][currCol] > dist) {
                grid[currRow][currCol] = dist;
                q.push(make_pair(currRow, currCol));
            }
        }
    }
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                bfs(grid, i, j);
            }
        }
    }
};
