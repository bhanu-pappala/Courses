#include <iostream>
#include <vector>

using std::vector;
using std::pair;
using std::cout;

vector<int> dfs_num;
void reach(vector<vector<int> > &adj, int x, int y) {
	if(x == y) {
		dfs_num[x] = 2;
		return ;
	}
	dfs_num[x] = 1;      // important step: we mark this vertex as visited
	for (int j = 0; j < (int)adj[x].size(); j++) {
		int v = adj[x][j];                      // v is a (neighbor, weight) pair
		if(v == y) {
			dfs_num[v] = 2;
			return ;
		}
		else if (dfs_num[v] == -1)         // important check to avoid cycle
			reach(adj, v, y);      // recursively visits unvisited neighbors v of vertex u
	}
}

int main() {
	size_t n, m;
	std::cin >> n >> m;
	vector<vector<int> > adj(n, vector<int>());
	for (size_t i = 0; i < m; i++) {
		int x, y;
		std::cin >> x >> y;
		adj[x - 1].push_back(y - 1);
		adj[y - 1].push_back(x - 1);
	}
	int x, y;
	dfs_num.assign(n, -1);
	std::cin >> x >> y;
	reach(adj, x - 1, y - 1);
	bool found = false;
	for(int i = 0; i < n; i++) {
		if(dfs_num[i] == 2) {
			found = true;
		}
	}
	cout << found ? 1 : 0 ;
}
