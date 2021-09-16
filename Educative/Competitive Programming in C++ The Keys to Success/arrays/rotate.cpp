#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ifstream cin("rotate.txt");

    int n, d;
    cin >> n >> d;
    vector<int> v(n);
    for(int i = 0; i < n; i++)
        cin >> v[i];

    vector<int> res(n);

    for(int i = n-d, j = 0; i < n; i++, j++)
        res[j] = v[i];
    for(int i = 0, j = d; i < n-d; i++, j++)
        res[j] = v[i];

    for(int i = 0; i < n; i++)
        cout << res[i] << " " ;
    return 0;

}
