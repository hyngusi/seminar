#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int INF = 1e9;

// H�m t?m c�y khung nh? nh?t b?ng thu?t to�n Prim
int Prim(vector<vector<int> >& graph) {
    int n = graph.size();
    vector<bool> visited(n, false); // ��nh d?u c�c �?nh �? th�m
    priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq; // H�ng �?i �u ti�n

    int minCost = 0;

    // B?t �?u t? �?nh 0
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
    int n; // S? �?nh
    cin >> n;

    vector<vector<int> > graph(n, vector<int>(n));

    // Nh?p ma tr?n tr?ng s?
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> graph[i][j];
            if (graph[i][j] == 0) {
                // N?u c� gi� tr? 0, ��nh d?u l� v� c�ng
                graph[i][j] = INF;
            }
        }
    }

    int minCost = Prim(graph);
    cout << "T?ng tr?ng s? c?a c�y khung nh? nh?t: " << minCost << endl;

    return 0;
}

