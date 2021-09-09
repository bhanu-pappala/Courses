#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll countSplitInv(vector<ll> B, vector<ll> C)
{
    int i, j, k;
    int count;
    int nb = B.size();
    int nc = C.size();
    vector<ll> temp;
    while(i < nb && j < nc)
    {
        if(B[i] < C[j])
        {
            temp[k] = B[i];
            i++;
        }
        else
        {
            temp[k] = C[j];
            j++;
            count += (nb - i);
        }
    k++;
    }
    while(i < nb)
    {
        temp[k] = B[i];
        i++;
        k++;
    }
    while(j < nc)
    {
        temp[k] = C[j];
        j++;
        k++;
    }
    return count;
}

ll arr_count(vector<ll> array)
{
    int n = array.size();
    ll count;
    if(n > 1)
    {
        int split_position = n / 2;
        vector<ll> left(array.begin(), array.begin() + split_position);
        vector<ll> right(array.begin() + split_position + 1, array.end());
        count += arr_count(left);
        count += arr_count(right);
        count += countSplitInv(left, right);
        return count;
    }
    else
    {
        return 0;
    }
    
}

int main() {
    ifstream input_stream("IntegerArray.txt");
    vector<ll> array;
    string line;
    while (getline(input_stream, line)) 
    {
    array.push_back(stoi(line));
    }
    int n = 50;
    
    vector<ll> sample;
    for(int i = 0; i< 50 ; i++) {
        sample[i] = array[i];
        
    }
    printf("%lld", arr_count(sample));
    return 0;
}