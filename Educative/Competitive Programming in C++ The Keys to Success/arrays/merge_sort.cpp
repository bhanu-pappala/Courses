#include <bits/stdc++.h>
using namespace std;

void merge(int a[], int b[], int c[], int n, int m)
{
    int i = 0, j = 0, l = 0;
    while (i < n && j < m)
    {
        if (a[i] < b[j])
            c[l++] = a[i++];
        else
            c[l++] = b[j++];
    }
    while (i < n)
        c[l++] = a[i++];
    while (j < m) 
        c[l++] = b[j++];
}

int main() 
{
    ifstream cin("merge_sort.txt");

    int n, m;
    cin >> n >> m;
    int a[n], b[m], c[n+m];
    for(int i = 0; i < n; i++)
        cin >> a[i];
    for(int i = 0; i < m; i++)
        cin >> b[i];

    merge(a, b, c, n, m);

    for(int i = 0; i < n+m; i++)
        cout << c[i] << " ";
    return 0;

}
