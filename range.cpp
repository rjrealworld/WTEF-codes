#include <iostream>
#include <vector>
using namespace std;

class Range {
    private:
        int a, b;
    
    public:
        //Constructors
        Range (int limit) {
            a = 1, b = limit;
        }
        Range(int start, int limit) {
            a = start, b = limit;
        }
        
        int minRange() {
            return a;
        }
        int maxRange() {
            return b;
        }
        int lengthOfRange() {
            return b - a;
        }
        bool contains(Range r) {
            return (r.minRange() >= a && r.maxRange() <= b);
        }
        bool contains(int val) {
            return (val >= a && val < b); //Since b is excluded
        }
        bool overlap (Range r) {
            return ((r.minRange() > a && r.minRange() < b) || (r.maxRange() > a && r.maxRange() < b)
                     || (b > r.minRange() && b < r.maxRange()) || (a > r.minRange() && a < r.maxRange()));
        }
        bool touching (Range r) {
            return ((r.minRange() == b) || (a == r.maxRange()));
        }
        bool disjoint (Range r) {
            return (!touching(r));
        }
        bool lessThan (Range r) { // a < b
            return (a < r.minRange() && lengthOfRange() < r.lengthOfRange());
        }
        Range combine (Range r) {

        }
};

int main() {
    Range r1(10, 20);
    Range r2(3, 30);
    cout << r1.minRange() << " " << r1.maxRange();
}