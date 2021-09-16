#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ifstream cin("subarray_sum.txt");

    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for(int i = 0; i < n; i++)
        cin >> a[i];

    vector<int> sum(n);
    sum[0] = a[0];

    for(int i = 1; i < n; i++)
        sum[i] = sum[i-1] + a[i];

    for(int i = 0; i < q; i++) 
    {
        int l, r;
        cin >> l >> r;
        l--; r--;

        int ans = sum[r];
        if (l > 0)
            ans -= sum[l-1];

        cout << ans ;
        cout << "\n";
    }
    return 0;

}
