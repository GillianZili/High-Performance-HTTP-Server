#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
using namespace std;

mutex mtx;
class A{
public:
    A(){
        cout<<"construct"<<endl;
    }
    ~A(){
        cout<<"destruct"<<endl;
    }
};

int main()
{
    A a;
    auto lambda = [](int x)
    {
        mtx.lock();
        //why no mutex will cause race condition in <<
        cout << "hello from thread: " << this_thread::get_id() << endl;
        cout << "argument passed in: " << x << endl;
        mtx.unlock();
    };
    vector<jthread> threads;
    for (int i = 0; i < 10; i++)
    {
        threads.emplace_back(lambda, 100);
    }
    // for (int i = 0; i < 10; i++)
    // {
    //     //join() blocks the current thread until the child thread complete their execution
    //     //otherwise the operating system may automatically call the thread's destructor, once the des detect the thread is not joinable, it will call terminate(), which casuing a core dump
    //     threads[i].join();
    // }
    mtx.lock();
    cout << "hello from my main thread" << endl;
    mtx.unlock();
    return 0;
}