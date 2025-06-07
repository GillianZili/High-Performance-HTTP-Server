#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
using namespace std;
mutex mtx;

int main(){
    int a=0;
    auto inc=[&](){
        mtx.lock();
        a+=1;
        mtx.unlock();
    };

    vector<thread> ts;
    for(int i=0;i<100000;i++){
        ts.push_back(thread(inc));
    }
    for(int i=0;i<100000;i++){
        ts[i].join();
    }
    cout<<a<<endl;
    return 0;
}