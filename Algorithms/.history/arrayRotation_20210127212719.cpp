// Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

#include <iostream>
using namespace std;

// Method 1


int main() {
    int arr[] = { 1, 2, 3, 4, 5, 6, 7 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
  
    // Function calling 
    leftRotate(arr, 2, n); 
    printArray(arr, n); 
  
    return 0; 
}