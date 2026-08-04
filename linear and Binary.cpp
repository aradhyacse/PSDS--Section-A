// LINEAR SEARCH--------------------------------------------

#include <iostream>
using namespace std;
int main() {
    int n, key;
    cout << "Enter size of array: ";
    cin >> n;
    int arr[n];
    cout << "Enter array elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << "Enter element to find: ";
    cin >> key;
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            cout << "Element found at index: " << i;
            return 0;
        }
    }
    cout << "Element not found (-1)";
    return 0;
}



// BINARY SEARCH---------------------------------------------------
#include <iostream>
using namespace std;
int main() {
    int n, key;
    cout << "Enter size of array: ";
    cin >> n;
    int arr[n];
    cout << "Enter sorted array elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << "Enter element to find: ";
    cin >> key;
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == key) {
            cout << "Element found at index: " << mid;
            return 0;
        }
        else if (arr[mid] < key) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    cout << "Element not found (-1)";
    return 0;
}