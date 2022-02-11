#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define pb push_back

using namespace std;

int t,k;

long long x1,y3,x2,y2;

vector<int> x,y;

void solve(){
    cin >> k;

    for (int p; p < k; p++){
            cin >> x1 >> y3 >> x2 >> y2; 
            x.pb(x1);
            x.pb(x2);
            y.pb(y3);
            y.pb(y2);
        }
    sort(begin(x), end(x));
    sort(begin(y), end(y));
    cout << x[k-1] << ' ' << y[k-1];


}



int main(){
    cin >> t;
    for (int i; i < t; i++){
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;

    }

    return 0;
}











