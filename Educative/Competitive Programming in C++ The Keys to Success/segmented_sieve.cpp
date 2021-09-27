#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream cin("sieve.txt");

    int n, m;
    cin >> n>> m;
    vector<int> is_prime(m-n+1, true);

    for(int i = 2; i * i <= m; i++)
    {
        int start = (((n-1)/i) + 1) * i;
        for(int j = start; j <= m; j+= i)
        {
            if (j >= n && j <= m)
                is_prime[j-n] = false;
        }
    }
    for(int i = 0; i < is_prime.size(); i++)
        if (is_prime[i])
            cout << i + n << " ";
}
