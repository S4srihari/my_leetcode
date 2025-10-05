class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<vector<int>> res;
        vector<vector<bool>> pac(m, vector<bool>(n, false));
        vector<vector<bool>> atl(m, vector<bool>(n, false));
        deque<pair<int, int>> pq, aq;

        for (int i = 0; i < m; i++) {
            pq.push_back({i, 0});
            aq.push_back({i, n - 1});
            pac[i][0] = true;
            atl[i][n - 1] = true;
        }
        for (int j = 0; j < n; j++) {
            pq.push_back({0, j});
            aq.push_back({m - 1, j});
            pac[0][j] = true;
            atl[m - 1][j] = true;
        }

        int dirs[5] = {0, 1, 0, -1, 0};
        auto bfs = [&](deque<pair<int, int>>& q, vector<vector<bool>>& ocean) {
            while (!q.empty()) {
                auto [x, y] = q.front();
                q.pop_front();
                for (int d = 0; d < 4; d++) {
                    int nx = x + dirs[d], ny = y + dirs[d + 1];
                    if (nx >= 0 && ny >= 0 && nx < m && ny < n &&
                        !ocean[nx][ny] && heights[nx][ny] >= heights[x][y]) {
                        ocean[nx][ny] = true;
                        q.push_back({nx, ny});
                    }
                }
            }
        };

        bfs(pq, pac);
        bfs(aq, atl);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pac[i][j] && atl[i][j])
                    res.push_back({i, j});
            }
        }
        return res;
    }
};