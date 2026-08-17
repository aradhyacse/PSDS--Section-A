#include <iostream>
using namespace std;

int main() {
    int queue[10] = {10, 20, 30};
    int n = 3;

    cout << "Original Queue: ";
    for (int i = 0; i < n; i++)
        cout << queue[i] << " ";
    cout << endl;

    // Enqueue Operation
    queue[n] = 40;
    n++;

    cout << "After Enqueue: ";
    for (int i = 0; i < n; i++)
        cout << queue[i] << " ";
    cout << endl;

    // Dequeue Operation
    int dequeued_item = queue[0];
    cout << "Dequeued Item: " << dequeued_item << endl;

    for (int i = 0; i < n - 1; i++)
        queue[i] = queue[i + 1];

    n--;

    cout << "After Dequeue: ";
    for (int i = 0; i < n; i++)
        cout << queue[i] << " ";
    cout << endl;

    return 0;
}