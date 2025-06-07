#include <iostream>
#include <thread>
#include <mutex>
#include <vector>
#include <condition_variable>
using namespace std;

condition_variable conv;
mutex mtx;

int main(){
    //to do: t1 & t2 take turns to check and pack fruits
    //suppose there are 3 kinds of fruits, each with 6
    vector<vector<string>> fruits(3,vector<string>(6,"picked"));
    int checked=-1,packed=-1;

    //t1 will be awaked until t2 finishes its execution
    //after finishing the execution, t2 will fall asleep until notified by t1
    thread check([&]{
        for(int i=0;i<3;i++){
            unique_lock<mutex> lock(mtx);
            conv.wait(lock, [&] { return checked == packed; });
            for(int j=0;j<6;j++){
                fruits[i][j]="checked";
            }
            checked=i;
            cout<<"fruit number "<<i+1<<" has been checked."<<endl;

            conv.notify_one();
        } 
    });

    thread pack([&]{
        for (int i = 0; i < 3; ++i) {
            unique_lock<mutex> lock(mtx);
            conv.wait(lock, [&] { return checked > packed; });
    
            for (int j = 0; j < 6; ++j) {
                fruits[checked][j] = "packed";
            }
            packed = checked;
            cout << "Fruit " << checked + 1 << " has been packed." << endl;
    
            conv.notify_one();
        }
    });

    check.join();
    pack.join();
    for(int i=0;i<3;i++){
        for(int j=0;j<6;j++){
            cout<<fruits[i][j]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
