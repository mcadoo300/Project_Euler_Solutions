#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int x = 0;
	int output = 0;
	for (int i = 2;i < 998;i++) {
		for (int j = 2;j < (998 - i);j++) {
			x = (i * i) + (j * j);
			if ((sqrt(x) + i + j) == 1000)
				output = i * j * sqrt(x);
		}
	}

	cout << output;
	system("pause");
	return 0;
}