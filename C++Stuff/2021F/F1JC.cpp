#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define pb push_back
#define vt vector
#define ll long long

using namespace std;

int solve(){
    int n;
    int ans = 0;
    string poo;
    vt<int> inters;
    cin >> n;
    cin >> poo;

    for (int i; i < n; i++){
        if (poo[i] == '1'){
            inters.pb(i);
        }
    }

    for (int i; i < n; i++){
        int lowest = 100000;
        if (poo[i] == '0'){
            for (int j; j < inters.size(); j++){
                int lowest = abs(inters[j] - i);
                if (int(abs(inters[j] - i)) < lowest){
                    lowest = int(abs(inters[j] - i));
                }
            }
        }
        cout << ans << endl;
        if (poo[i] == '0'){
            ans += lowest;
        }
    }

    return ans;

}


int main(){
    int t, pee;
    cin >> t;
    for (int i; i < t; i++){
        pee = solve();
        cout << "Case #" << i+1 << ": " << pee;
        cout << endl;
    }

    return 0;
}



