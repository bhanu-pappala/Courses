#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>

#define ll long long

using namespace std;

namespace helper{
template<typename T>
void swap(T& a, T& b)
{
    T c(a);
    a = b;
    b = c;
}
template<typename T>
void printVec(const vector<T>& v, int left, int right)
{
    for(int i = left; i < right; ++i)
    {
        cout << v[i] << " ";
    }
    cout << "\n";
}
template<typename T>
void printVec(const vector<T>& v)
{
    for(auto& p : v)
    {
        cout << p << " ";
    }
    cout << "\n";
}

}


template<typename T>
int partition_0(vector<T>& in, int lo, int hi)
{

    //cout << "partition:lo=" << lo << "hi=" << hi << "\n";
    //helper::printVec<int>(in);
    T pivot = in[lo];
    int i = lo + 1;
    for(int j = lo + 1; j <= hi ; ++j)
    {
        if(in[j] < pivot)
        {
    //       fprintf(stdout, "i=%d;j=%d;in[i]=%d;in[j]=%d\n",i,j,in[i],in[j]);
            helper::swap<T>(in[j], in[i]);
            i++;
        }
    }
    helper::swap<T>(in[i - 1], in[lo]);
    return i - 1;
}

template<typename T>
int partition_1(vector<T>& in, int lo, int hi)
{

//    cout << "partition:lo=" << lo << "hi=" << hi << "\n";
//    helper::printVec<int>(in);
    helper::swap<T>(in[hi],in[lo]);
    T pivot = in[lo];
    int i = lo + 1;
    for(int j = lo + 1; j <= hi ; ++j)
    {
        if(in[j] < pivot)
        {
//           fprintf(stdout, "i=%d;j=%d;in[i]=%d;in[j]=%d\n",i,j,in[i],in[j]);
            helper::swap<T>(in[j], in[i]);
            i++;
        }
    }
    helper::swap<T>(in[i - 1], in[lo]);
    //helper::printVec<int>(in);
    return i - 1;
}

template<typename T>
T median(const T& a, const T& b, const T& c)
{
    return max(min(a,b), min(max(a,b),c));
}
template<typename T>
int medianPivot(vector<T>& in, int lo, int mid, int hi)
{
    T _median = median<T>(in[lo],in[mid],in[hi]);
    int k;
    if(_median == in[lo]) k = lo;
    else if(_median == in[mid]) k = mid;
    else if(_median == in[hi]) k = hi;
    return k;
}

template<typename T>
int partition_2(vector<T>& in, int lo, int hi)
{

//    cout << "partition:lo=" << lo << "hi=" << hi << "\n";
//    helper::printVec<int>(in);
    int len = (hi - lo + 1);
    int mid;
    if(len % 2 == 0) mid = lo + len / 2 - 1;
    else mid = lo + len / 2;
    int ind = medianPivot<T>(in,lo,mid,hi);
    helper::swap<T>(in[ind], in[lo]);
    T pivot = in[lo];
    int i = lo + 1;
    for(int j = lo + 1; j <= hi ; ++j)
    {
        if(in[j] < pivot)
        {
//           fprintf(stdout, "i=%d;j=%d;in[i]=%d;in[j]=%d\n",i,j,in[i],in[j]);
            helper::swap<T>(in[j], in[i]);
            i++;
        }
    }
    helper::swap<T>(in[i - 1], in[lo]);
    return i - 1;
}
template<typename T>
void sort(vector<T>& in, int lo, int hi, int* cnt)
{
    if(lo < hi)
    {
        int p = partition_2<T>(in, lo, hi);
        // fprintf(stdout, "p=%d\n", p);
        (*cnt) += hi - lo ;
        sort<T>(in, lo, p - 1 , cnt);
        sort<T>(in, p + 1, hi, cnt);
    }
}

int main(int argc, char* argv[])
{
    ifstream input_stream("QuickSort.txt");
    vector<int> input;
    string line;
    int cnt = 0;
    int num = 10000;
    while (getline(input_stream, line)) 
    {
        input.push_back(stoi(line));
    }
//    helper::printVec<int>(input);
    sort<int>(input, 0, num - 1, &cnt);
    cout << "cnt=" << cnt << "\n";
    return 0;

}