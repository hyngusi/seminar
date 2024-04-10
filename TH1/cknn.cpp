#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int INF = 1e9;

// Hàm t?m cây khung nh? nh?t b?ng thu?t toán Prim
int Prim(vector<vector<int> >& graph) {
    int n = graph.size();
    vector<bool> visited(n, false); // Ðánh d?u các ð?nh ð? thãm
    priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq; // Hàng ð?i ýu tiên

    int minCost = 0;

    // B?t ð?u t? ð?nh 0
    pq.push(make_pair(0, 0));

    while (!pq.empty()) {
        int u = pq.top().second;
        int w = pq.top().first;
        pq.pop();

        if (visited[u]) continue;

        visited[u] = true;
        minCost += w;

        for (int v = 0; v < n; ++v) {
            if (!visited[v] && graph[u][v] != INF) {
                pq.push(make_pair(graph[u][v], v));
            }
        }
    }

    return minCost;
}

int main() {
    int n; // S? ð?nh
    cin >> n;

    vector<vector<int> > graph(n, vector<int>(n));

    // Nh?p ma tr?n tr?ng s?
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> graph[i][j];
            if (graph[i][j] == 0) {
                // N?u có giá tr? 0, ðánh d?u là vô cùng
                graph[i][j] = INF;
            }
        }
    }

    int minCost = Prim(graph);
    cout << "T?ng tr?ng s? c?a cây khung nh? nh?t: " << minCost << endl;

    return 0;
}

