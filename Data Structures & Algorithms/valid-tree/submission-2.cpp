class Solution {
    bool dfsVisit(vector<vector<int>> &adjMat, vector<bool> &visited, vector<int> &pred, int i) {
        visited[i] = true;
        bool res = true;
        for (int neighbor : adjMat[i]) {
            if (pred[i] == neighbor)
                continue;
            if (visited[neighbor])
                return false;
            
            pred[neighbor] = i;
            res &= dfsVisit(adjMat, visited, pred, neighbor);
            if (!res)
                return false;
        }

        return true;
    }
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adjMat(n);

        for (vector<int> edge : edges) {
            adjMat[edge[0]].push_back(edge[1]);
            adjMat[edge[1]].push_back(edge[0]);
        }

        vector<int> pred(n, -1);
        vector<bool> visited(n);
        bool res = dfsVisit(adjMat, visited, pred, 0);

        if (!res)
            return false;

        for (bool v : visited) {
            if (!v)
                return false;
        }

        return true;
    }
};
