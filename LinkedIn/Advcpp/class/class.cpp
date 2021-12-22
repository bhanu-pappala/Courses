#include<cstdio>
using namespace std;

class c1 {
	int i = 0;
public:
	void setValue(const int & value){
		i = value;
	}
	int getValue() const {
		return i;
	}
};

int main()
{
	const int i = 98;
	c1 o1;
	o1.setValue(i);
	printf("Value is %d\n", o1.getValue());
	return 0;
}
