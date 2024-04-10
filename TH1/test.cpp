#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <limits>

using namespace std;

const double INF = numeric_limits<double>::max();

// Ð?nh ngh?a c?u trúc cho ði?m
struct Point {
    double x, y;
};

// Hàm tính kho?ng cách Euclidean gi?a hai ði?m
double euclideanDistance(const Point& p1, const Point& p2) {
    return sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
}

// Hàm gi?i bài toán TSP b?ng ð? quy và lýu k?t qu? vào dp
double tspDP(vector<vector<double> >& dp, vector<int>& path, int mask, int current, const vector<Point>& points) {
    int n = points.size();

    // N?u ð? duy?t qua t?t c? thành ph?, tr? v? kho?ng cách v? thành ph? ban ð?u
    if (mask == (1 << n) - 1) {
        return euclideanDistance(points[current], points[0]);
    }

    // N?u ð? tính toán trý?c ðó, tr? v? giá tr? ð? tính
    if (dp[mask][current] != -1) {
        return dp[mask][current];
    }

    double minDist = INF;
    int next = -1;

    // Duy?t qua t?t c? thành ph? chýa ðý?c thãm
    for (int city = 0; city < n; city++) {
        if (!(mask & (1 << city))) {
            double dist = euclideanDistance(points[current], points[city]) + tspDP(dp, path, mask | (1 << city), city, points);
            if (dist < minDist) {
                minDist = dist;
                next = city;
            }
        }
    }

    // Lýu k?t qu? và thành ph? ti?p theo vào dp và path
    dp[mask][current] = minDist;
    path[current] = next;

    return minDist;
}

// Hàm in ra ðý?ng ði t?i ýu
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
        cout << "S? d?ng: " << argv[0] << " <t?p ð?u vào>" << endl;
        return 1;
    }

    string inputFileName = argv[1];
    ifstream inputFile(inputFileName);
    if (!inputFile) {
        cout << "L?i: Không th? m? t?p ð?u vào." << endl;
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

    cout << "Kho?ng cách TSP t?i thi?u: " << minDistance << endl;
    printPath(path);

    return 0;
}

