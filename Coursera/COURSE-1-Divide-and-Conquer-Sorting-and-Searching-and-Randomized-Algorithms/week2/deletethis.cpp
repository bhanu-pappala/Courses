#include <bits/stdc++.h>
#include <vector>

using namespace std; 

int main() {
	map<string, int> m;
	m["monkey"] = 3;
	m["donkey"] = 4;
	for (auto x : m){
		cout << x.first << " " << x.second << '\n';
	}
}