#include<cstdio>
#include<iostream>
using namespace std;

class Rational
{
	int _n = 0;
	int _d = 1;
public:
	Rational(int numerator = 0, int denominator = 1) : _n(numerator), _d(denominator) {};
	Rational(const Rational & rhs) : _n(rhs._n), _d(rhs._d) {};
	~Rational();
	int numerator() const {return _n;};
	int denominator() const {return _d;};

	Rational & operator = (const Rational &);
	Rational operator + (const Rational &) const;
	Rational operator - (const Rational &) const;
	Rational operator * (const Rational &) const;
	Rational operator / (const Rational &) const;
};

Rational & Rational::operator = (const Rational & rhs) {
	if(this != &rhs){
		_n = rhs.numerator();
		_d = rhs.denominator();
	}
	return *this;
}

Rational Rational::operator + (const Rational & rhs) const {
	return Rational((_n * rhs.denominator()) + (_d * rhs.numerator()), _d * rhs.denominator());
}

Rational Rational::operator - (const Rational & rhs) const {
	return Rational((_n * rhs.denominator()) - (_d * rhs.numerator()), _d * rhs.denominator());
}

Rational Rational::operator * (const Rational & rhs) const {
	return Rational(_n * rhs.numerator(), _d * rhs._d);
}

Rational Rational::operator / (const Rational & rhs) const {
	return Rational(_n * rhs._d, _d * rhs._n);
}

Rational::~Rational() {
	_n = 0;
	_d = 1;
}

std::ostream & operator << (std::ostream & o, const Rational & rhs) {
	if(rhs.denominator() == 1) {
		return o << rhs.numerator();
	}
	else {
		return o << rhs.numerator() << "/" << rhs.denominator();
	}
}

int main() {
    
    Rational a = 7;        // 7/1
    cout << "a is: " << a << endl;
    Rational b(5, 3);    // 5/3
    cout << "b is: " << b << endl;
    Rational c = b;        // copy constructor
    cout << "c is: " << c << endl;
    Rational d;            // default constructor
    cout << "d is: " << d << endl;
    d = c;                // assignment operator
    cout << "d is: " << d << endl;
    Rational & e = d;    // reference// so no object is created since it is reference
    d = e;                // assignment to self!
    cout << "e is: " << e << endl;
    
    cout << a << " + " << b << " = " << a + b << endl;
    cout << a << " - " << b << " = " << a - b << endl;
    cout << a << " * " << b << " = " << a * b << endl;
    cout << a << " / " << b << " = " << a / b << endl;
    a/b;

    return 0;
}

