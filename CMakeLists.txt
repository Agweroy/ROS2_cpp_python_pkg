cmake_minimum_required(VERSION 3.5)
project(cpp_python_pkg)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)

# C++ executable installation.
include_directories(include)

add_executable(cpp_exec src/cpp_node.cpp)
ament_target_dependencies(cpp_exec rclcpp)

install(TARGETS
cpp_exec
DESTINATION lib/${PROJECT_NAME})

# python executable instllations

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
scripts/python_node.py
DESTINATION lib/${PROJECT_NAME})
 

ament_package()
