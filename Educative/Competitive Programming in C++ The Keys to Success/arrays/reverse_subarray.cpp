#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ifstream cin("reverse_subarray.txt");

    int n, q;
    cin >> n >> q;
    vector<int> a(n, 0);
    for(int i = 0; i < n; i++)
        cin >> a[i];

    for(int i = 0; i < q; i++) 
    {
        int l, r;
        cin >> l >> r;
        l--; r--;

        for(int p1 = l, p2 = r; p1 < p2; p1++, p2--)
            swap(a[p1], a[p2]);

        for(int j = 0; j < n; j++)
            cout << a[j] << " ";
        cout << "\n";
    }
    return 0;

}
