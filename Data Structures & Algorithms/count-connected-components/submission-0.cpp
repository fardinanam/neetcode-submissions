class Solution {
    void dfsVisit(int i, vector<vector<int>> &graph, vector<bool> &visited) {
        visited[i] = true;

        for (int n : graph[i]) {
            if (!visited[n]) {
                dfsVisit(n, graph, visited);
            }
        }
    }

public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<bool> visited(n, false);

        vector<vector<int>> graph(n);
        for (vector<int> edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                count++;
                dfsVisit(i, graph, visited);
            }
        }

        return count;
    }
};
