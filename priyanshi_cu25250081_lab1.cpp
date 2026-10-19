/*#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> arr = {10, 20, 30, 40, 50};

    cout << "Vector before pop_back(): ";

    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }

    arr.pop_back();

    cout << "\nVector after pop_back(): ";

    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
}*/



#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> arr;
    int n, element;

    cout << "Enter the number of elements: ";
    cin >> n;

    cout << "Enter the elements:\n";

    for (int i = 0; i < n; i++)
    {
        cin >> element;
        arr.push_back(element);
    }

    cout << "\nElements in the vector are: ";

    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
}