#include <iostream>
#include <vector>

using std::vector;
using std::pair;

vector<int> dfs_num;

void dfs(vector<vector<int>> &adj, int u) {
	dfs_num[u] = 1;
	for (int j = 0; j < (int)adj[u].size(); j++) {
		int v = adj[u][j];
		if (dfs_num[v] == -1)
			dfs(adj, v);
	}
}

int number_of_components(vector<vector<int> > &adj) {
	int res = 0;
	for(int i = 0; i < (int)adj.size(); i++) {
		if(dfs_num[i] == -1) {
			res += 1;
		}
		dfs(adj, i);
	}
	return res;
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
  dfs_num.assign(n, -1);
  std::cout << number_of_components(adj);
}
