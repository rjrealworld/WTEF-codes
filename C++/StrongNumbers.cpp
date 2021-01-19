#include <iostream>
#include <vector>
#include <string>
using namespace std;
 
vector <long int> factorial = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800 , 87178291200};

bool isStrong(int a) {
    string num = to_string(a);
    int sum = 0;
    for (int i = 0; i < num.length(); i++) {
        sum += factorial[num[i] - 48];
    }
    return sum == a;
}

vector <long int> strong_numbers (int num) {
    vector <long int> result;
    for (long int i = 100000000; i <= num; i++) {
        if (isStrong(i)) {
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    long int n = 87178291200;
    vector <long int> answer = strong_numbers(n);
    for (const long int c: answer) {
        cout << c << endl;
    }
    return 0;
}
