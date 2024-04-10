#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <limits>

using namespace std;

const double INF = numeric_limits<double>::max();

// �?nh ngh?a c?u tr�c cho �i?m
struct Point {
    double x, y;
};

// H�m t�nh kho?ng c�ch Euclidean gi?a hai �i?m
double euclideanDistance(const Point& p1, const Point& p2) {
    return sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
}

// H�m gi?i b�i to�n TSP b?ng �? quy v� l�u k?t qu? v�o dp
double tspDP(vector<vector<double> >& dp, vector<int>& path, int mask, int current, const vector<Point>& points) {
    int n = points.size();

    // N?u �? duy?t qua t?t c? th�nh ph?, tr? v? kho?ng c�ch v? th�nh ph? ban �?u
    if (mask == (1 << n) - 1) {
        return euclideanDistance(points[current], points[0]);
    }

    // N?u �? t�nh to�n tr�?c ��, tr? v? gi� tr? �? t�nh
    if (dp[mask][current] != -1) {
        return dp[mask][current];
    }

    double minDist = INF;
    int next = -1;

    // Duy?t qua t?t c? th�nh ph? ch�a ��?c th�m
    for (int city = 0; city < n; city++) {
        if (!(mask & (1 << city))) {
            double dist = euclideanDistance(points[current], points[city]) + tspDP(dp, path, mask | (1 << city), city, points);
            if (dist < minDist) {
                minDist = dist;
                next = city;
            }
        }
    }

    // L�u k?t qu? v� th�nh ph? ti?p theo v�o dp v� path
    dp[mask][current] = minDist;
    path[current] = next;

    return minDist;
}

// H�m in ra ��?ng �i t?i �u
void printPath(const vector<int>& path) {
    cout << "Optimal Path: ";
    int current = 0;
    while (true) {
        cout << current + 1 << " -> ";
        current = path[current];
        if (current == 0) {
            break;
        }
    }
    cout << "1" << endl;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cout << "S? d?ng: " << argv[0] << " <t?p �?u v�o>" << endl;
        return 1;
    }

    string inputFileName = argv[1];
    ifstream inputFile(inputFileName);
    if (!inputFile) {
        cout << "L?i: Kh�ng th? m? t?p �?u v�o." << endl;
        return 1;
    }

    int numCities;
    inputFile >> numCities;

    vector<Point> points(numCities);
    for (int i = 0; i < numCities; i++) {
        inputFile >> points[i].x >> points[i].y;
    }

    vector<vector<double>> dp(1 << numCities, vector<double>(numCities, -1));
    vector<int> path(numCities, -1);
    double minDistance = tspDP(dp, path, 1, 0, points);

    cout << "Kho?ng c�ch TSP t?i thi?u: " << minDistance << endl;
    printPath(path);

    return 0;
}

