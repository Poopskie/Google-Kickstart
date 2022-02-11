#include <iostream>
#include <string>

using namespace std;

int n;
int a,d,m;
long long c;
string order;


string solve(){
    for (int i; i < a; i ++){
        if (order[i] == 'D'){
            d--;
            c += m;
        } else{
            c--;
        }
        if (d < 0){
            return "NO";
        }
        if ((order.rfind('D') <= i) || (order.rfind('D') == string::npos)){
            return "YES";
        }else
        if ((c < 0) and (order.rfind('D') > i)){
            return "NO";
        }
        

    }   
    return "YES";

}



int main(){
    cin >> n;
    for (int i; i<n; i++){
        cin >> a >> d >> c >> m;
        cin >> order;
        cout << "Case #" << i+1 << ": " << solve() << endl;
    }

    return 0;
}





