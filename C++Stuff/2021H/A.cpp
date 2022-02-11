#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define pb push_back
#define vt vector
#define ll long long

using namespace std;

string s;
string f;
string letters = "abcdefghijklmnopqrstuvwxyz";
vt<int> snum, fnum;


int solve(){
    int ans;

    cin >> s;
    cin >> f;

    for (int i; i < s.size(); i++){
        for(int x; x < letters.size(); x++){
            if (s[i] == letters[x]){
                snum.pb(x);
            }
        }
    }
    for (int i; i < f.size(); i++){
        for(int x; x < letters.size(); x++){
            if (f[i] == letters[x]){
                fnum.pb(x);
            }
        }
    }

//    sort(begin(snum), end(snum));
  //  sort(begin(fnum), end(fnum));

    for (int i; i< snum.size(); i++){
        int min = 25;
        for (int x; x < fnum.size(); x++){
            if ((abs(snum[i] - fnum[x])) < min){
                min = (abs(snum[i] - fnum[x]));
            } 
            if ((abs(snum[i] - (fnum[x]+26))) < min){
                min = (abs(snum[i] - (fnum[x]+26)));
            } 
            if ((abs((26+snum[i]) - fnum[x])) < min){
                min = (abs((26+snum[i]) - fnum[x]));
            } 
        }
        ans += min;
    }

    return ans;
}


int main(){
    int t;
    cin >> t;
    int final;
    for (int i; i < t; i++){
        final = solve();
        cout << "Case #" << i+1 << ": " << final << endl;
    }

    return 0;
}


















