#include <bits/stdc++.h>
#include <string>
using namespace std; 
#define ll long long

ll karatsuba_mul(ll num1,ll num2, ll n) {
	if ((num1 < 10) || (num2 < 10))
        return num1*num2;
    int splitPosition = n / 2;
    string num1Str = num1;
    string num2Str = num2;
    num1Str.copy(h1,0, splitPosition);
    num2Str.copy(l1,splitPosition, );
    ll high1 = num1Str.copy(,13,0);
    ll low1
    ll high2 
    ll low2


int main() {
	ll num1;
	ll num2;
	ll n = to_string(num1).length();
	answer = karatsuba_mul(x, y, n);
	cout << answer << endl;
}
