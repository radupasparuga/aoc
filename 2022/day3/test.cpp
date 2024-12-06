#include <iostream>

using namespace std;

int main() {
    int test[5][10];
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 10; ++j) {
            test[i][j] = 1;
        }
    }
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 10; ++j) {
            cout << test[i][j] << ' ';
        }
        cout << endl;
    }
    return 0;
}
