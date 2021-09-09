#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <sstream>
#include <ctime>
#include <list>
#include <utility>
#include <algorithm>
#include <climits>
using namespace std;

const string fileName = "kargerMinCut.txt";
const int REPEAT_NUM = 10000;
//expected result : 2
//cuts are[( 1, 7 ), ( 4, 5 )]
void readFile( string fileName, vector<list<int>> &graph );
int getEdgeNumber( vector<list<int>> &graph );
pair<int, int> getIndex( vector<list<int>> &graph, int edgeIndex );
int getValue( vector<list<int>> &graph, int node1Index, int node2Index );
void mergeTwoNode( vector<list<int>> &graph, int node1Val, int node2Val );
int getNodeNumber( vector<list<int>> &graph );
int kargerMinCut( vector<list<int>> graph );

int main() {
	vector<list<int>> graph;
	list<int> dummyHead;
	graph.push_back( dummyHead );
	readFile( fileName, graph );

	int count = INT_MAX;
	for( int i = 0; i < REPEAT_NUM; i++ ) {
		count = min( count, kargerMinCut( graph ) );
	}
	cout << count << endl;
	return count;
}

void readFile( string fileName, vector<list<int>> &graph ) {
	fstream myFile;
	myFile.open( fileName );

	if( !myFile.is_open() ) cerr << "file doesn't opened!" << endl;
	int vertexLabel;
	string numberStr;
	stringstream ss;
	while( myFile >> vertexLabel, getline( myFile, numberStr ) ) {
		ss << numberStr;
		list<int> data;
		while( true ) {
			int number;
			ss >> number;
			if( !ss ) break;
			data.push_back( number );
		}
		graph.push_back( data );
		ss.str( "" );
		ss.clear();
	}

	myFile.close();
}

int getEdgeNumber( vector<list<int>> &graph ) {
	int totalEdgeNumber = 0;
	for( int i = 1; i < graph.size(); i++ ) totalEdgeNumber += graph[i].size();
	return totalEdgeNumber;
}

pair<int, int> getIndex( vector<list<int>> &graph, int edgeIndex ) {
	for( int i = 1; i < graph.size(); i++ ) {
		if( graph[i].size() == 0 )continue;

		if( edgeIndex > graph[i].size() - 1 ) edgeIndex -= graph[i].size();
		else return make_pair( i, edgeIndex );
	}
}

int getValue( vector<list<int>> &graph, int node1Index, int node2Index ) {
	int index = 0;
	for( list<int>::iterator it = graph[node1Index].begin(); it != graph[node1Index].end(); it++ ) {
		if( index == node2Index ) return *it;
		else index++;
	}
}

void mergeTwoNode( vector<list<int>> &graph, int node1Val, int node2Val ) {
	//merge node2 to node1
	list<int> &node1 = graph[node1Val];
	list<int> &node2 = graph[node2Val];

	//1.move node2's adjency nodes to node1
	graph[node1Val].splice( node1.end(), node2 );
	//2.replace all occurence of node2 as node1's value
	for( int i = 1; i < graph.size(); i++ ) {
		if( graph[i].size() == 0 )continue;

		for( list<int>::iterator it = graph[i].begin(); it != graph[i].end(); it++ ) {
			if( *it == node2Val )*it = node1Val;
		}
	}
	//3.remove self loop in node1
	node1.remove( node1Val );

}

int getNodeNumber( vector<list<int>> &graph ) {
	int nodeNumber = 0;
	for( int i = 1; i < graph.size(); i++ ) {
		if( graph[i].size() != 0 )nodeNumber++;
	}
	return nodeNumber;
}

int kargerMinCut( vector<list<int>> graph ) {
	while( getNodeNumber( graph ) > 2 ) {
		srand( time( NULL ) );

		int totaleEdgeNumber = getEdgeNumber( graph );
		// edgeIndex start from 0
		int edgeIndex = rand() % totaleEdgeNumber;
		pair<int, int> index = getIndex( graph, edgeIndex );

		// merge val2 to val1 
		int val1 = index.first;
		int val2 = getValue( graph, index.first, index.second );

		mergeTwoNode( graph, val1, val2 );
	}

	int count = INT_MAX;
	for( int i = 0; i < graph.size(); i++ ) {
		if( graph[i].size() == 0 )continue;
		count = min( count, ( int )graph[i].size() );
	}

	return count;
}