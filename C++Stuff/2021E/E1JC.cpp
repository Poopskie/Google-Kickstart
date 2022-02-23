#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#define pb push_back
#define vt vector
#define ll long long

using namespace std;

void solve(){
    string S;
    char newCarr[S.size()] = {'^'};
    char letters[S.size()];
    cin >> S;

    for (int i = 0; i <S.size(); i++){
        letters[i] = S[i];
    }

    vt<char> poo;

    for (int i = 0; i < S.size(); i++){
        for (int j = 0; j < S.size(); j++){
            if ((letters[j] != S[i]) && (letters[j] != '_')){
                poo.pb(letters[j]); // dude idk why but ig in c++ if u change the value
                newCarr[i] = poo[i]; // for example poo = pee, then i change pee = "doggy" then poo also becomes "doggy"
                letters[j] = '_'; // like what?
            }
        }   
    }
    for (int i = 0; i < S.size(); i ++){
        cout << newCarr[i];
        cout << letters[i];
    }

    if (newCarr[S.size()-1] != '^'){
        for (int i = 0; i < S.size(); i ++){
            cout << newCarr[i];
        }
    } else{
        cout << "IMPOSSIBLE";
    }




}


int main(){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }

    return 0;
}



