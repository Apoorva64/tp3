cmake_minimum_required(VERSION 3.10)
project(tp3)
#openmp
find_package(OpenMP REQUIRED)
set(CMAKE_CXX_STANDARD 17)

# RELEASE
set(CMAKE_CXX_FLAGS_RELEASE "-O3" "-fopenmp" "-lm")

add_executable(tp3_openmp main.cpp)
target_link_libraries(tp3_openmp OpenMP::OpenMP_CXX)


add_executable(tp3 main.cpp)
