#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int main() {
    system("cls");

    //Đọc file
    freopen("in.txt", "r", stdin);
    int a, b;
    cin >> a >> b;

    //Ghi file
    freopen("out.txt", "w", stdout);
    cout << b << " " << a;

    //Chuyển stream cin về console (chịu, dòng dưới không đúng)
    freopen("CON", "r", stdin);
    int c = 0, d = 0;
    cin >> c >> d;

    //Chuyển stream cout về console
    freopen("CON", "w", stdout);
    cout << c << " " << d << endl;

    cout << "end of program" << endl;
    return 0;
}