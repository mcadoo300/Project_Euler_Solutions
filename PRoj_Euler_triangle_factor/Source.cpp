#include <iostream>
#include <cmath>
#include <algorithm>
#include <list>

using namespace std;

//check if x is prime
//input: long long
//return: booleanl
bool isPrime(long x) {
	for (long i = 2;i < (floor(x / 2)+1);i++)
		if (fmod(x, i) == 0)
			return false;

	return true;
}

list<int> primeFactors(long x) {
	list<int>returnList = {};//list of exponents
	list<long>factorList = {};
	bool isFactored = false;//flag for when x is completely factored
	bool isFactor = true;//flag for if a particular prime is factor

	long primeFactor = 2;
	double primeExp = 1;
	while (!isFactored) {

		while (isFactor) {
			int test = fmod(x, (pow(primeFactor, primeExp)));

			if (test == 0)
				primeExp++;
			else
				isFactor = false;
		}
		isFactor = true;

		//if primeExp>1 add primeExp to list
		if (primeExp > 1) {
			returnList.push_front((int)primeExp);
			factorList.push_front((int)primeFactor);
		}
		primeExp = 1;

		list<int> ::iterator it1;
		list<long> ::iterator it2= factorList.begin();

		long factorForm=1;//product of factors

		for (it1 = returnList.begin();it1 != returnList.end();it1++) {
			//cout << *it2  << ' ' << *it1 << '\n';
			//cout << pow(*it2, (*it1 - 1)) << '\n';
			factorForm = factorForm * (pow(*it2, (*it1-1)));
			it2++;
		}
		if (factorForm == x)
			isFactored = true;
		else
		{
			factorForm = 1;
			primeFactor++;
			bool prime = isPrime(primeFactor);
			while (!prime) {
				primeFactor++;
				prime = isPrime(primeFactor);
			}
				
		}

	}
	return returnList;
}
//calculate number of divisors
int numDivisors(long x) {

	list<int> divisorExp= primeFactors(x);

	int numDivisors = 1;
	list<int> ::iterator it1;
	for (it1 = divisorExp.begin();it1 != divisorExp.end();it1++) {
		numDivisors = numDivisors * (*it1);
	}
	return numDivisors;

}

int main() {

	bool flag = false;
	long i = 0;
	long k = 1;
	while (!flag) {
		i = i + (k);
		cout << i << endl;
		cout << numDivisors(i) << endl;
		if (numDivisors(i) > 500)
			flag = true;
		k++;
	}
	cout << i;

	system("pause");
	return 0;
}