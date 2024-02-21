#include <iostream>
#include <cmath>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <chrono>

int MAX_THREADS = 16;

void prefix_sum_sequntial(unsigned long long *arr, unsigned long long n) {
    unsigned long long sum = 0;
    for (unsigned long long i = 0; i < n; i++) {
        sum += arr[i];
        arr[i] = sum;
    }
}

void prefix_sum(unsigned long long *arr,unsigned long long *tmp, unsigned long long n) {
    unsigned long long log_n = (unsigned long long) log2(n);
    for (unsigned long long i = 0; i <= log_n; i++) {
#ifdef _OPENMP
        #pragma omp parallel for num_threads(MAX_THREADS)
#endif
        for (unsigned long long j = 0; j < n; j++) {
            if (j >= (1 << i)) {
                tmp[j] = arr[j] + arr[j - (1 << i)];
            } else {
                tmp[j] = arr[j] + 0;
            }
        }
        unsigned long long *tmp2 = arr;
        arr = tmp;
        tmp = tmp2;
    }
}

int main(int argc, char *argv[]) {
    // get size with command line argument
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <size> <threads>" << std::endl;
        return 1;
    }
    unsigned long long n = std::stoull(argv[1]);
    MAX_THREADS = std::stoi(argv[2]);
    unsigned long long *arr = new unsigned long long[n];
    unsigned long long *tmp = new unsigned long long[n];
    for (unsigned long long i = 0; i < n; i++) {
        arr[i] = rand() % 100000000000;
    }
    auto start = std::chrono::high_resolution_clock::now();
    prefix_sum(arr, tmp, n);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << elapsed.count();
    delete[] arr;
    delete[] tmp;
}
