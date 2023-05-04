**HOW TO CREATE A PACKAGE FOR BOTH C++ AND PYTHON NODES**

Unlike ros1 packages which can contain both ```C++``` and ```python``` nodes by default, ros2 packages have to be assigned a ```C++```or python build type during the package creation.
In ros2, when you start to create a package, you have to specify if the package is going to be a C++ package or a Python package with either ament_cmake(for ```C++```) or ```ament_python```(for a python package).
ament_cmake and ament_python are called build types and will tell ros2 if your package is a C++ or python.


But is it possible to have a ros2 package with both C++ and python nodes??
the answer is YES!!!! the steps bellow shows how to create a ros2 combined package.

You first have to learn how to create a standard ros2 C++ and python package.

**TABLE OF CONTENT**
    

**1. CREATE A STANDARD C++ AND PYTHON PACKAGE**

      1.1 Add a C++ node and a header file.
      1.2 Add a python node and a module to import file
      1.3 ros2 package architecture with both python and C++ nodes.

**2. CONFIGORE YOUR ROS2 PACKAGE FOR BOTH C++ AND PYTHON**
        
      2.1 Package.xml edition
      2.2 CMakeList.txt
      2.3 Build and run your ros2 C++ and python nodes.



**1. First we create a standard C++ and python package.**

First create the package with the ament_cmake build type.
you can name the package say "cpp_python_pkg"

      $ mkdir -p ros2_wks/src
      $ cd ros2_wks/src
      $ ros2 pkg create cpp_python_pkg --build-type amen_cmake.

For now the package architecture looks like this:

                      
                    .
                    └── cpp_python_pkg
                        ├── CMakeLists.txt
                        ├── include
                        │   └── cpp_python_pkg
                        ├── package.xml
                        └── src
  
       

this is the base for a basic C++ package and from here will will add necessary files and configuration for python.

***1.1 We add the C++ (`.cpp`) file and the `.hpp` header file***

let's add a .cpp and file in the src/ directory, and a .hpp header file in the include/cpp_python_pkg/ directory. No need to create new folders here.

       $ cd cpp_python_pkg/
       $ touch src/cpp_node.cpp
       $ touch include/cpp_python_pkg/cpp_header.hpp

you have to  include the cpp_header.hpp if your cpp_node.cpp file needs it #include "cpp_python_pkg/cpp_header.hpp"

    
***1.2 Adding the python node file and import module file***

let's setup the package so it can also have python nodes.

       $ mkdir cpp_python_pkg
       $ touch cpp_python_pkg/__init__.py
       $ mkdir scripts

makde sure the first folder has the exact name of the package. Inside this folder we create an empty __init__.py file. This is something that is automatically created when you create a standard python package.


This folder will host any library and module we want to use or export.

then we create the scripts/ folder. in the scripts folder, we will place our executables(nodes).

Now that we have the structure lets add one python module and one node. 
        
        $ touch cpp_python_pkg/module_to_import.py
        $ touch scripts/python_node.py

don't forget to add the shebang line in your python_node.py. usually the first line of your code.

        #!/usr/bin/env python3

This is something you don't have to do in a standared ros2 python package since it is already managed for you but with this modification, if you don't add this line, you'll get an error notification when you try to start the node with ```ros2 run``` or from a launch file. 
    
if you want to be able to modify your code and re-run it without recompilling every time, or if you want to start your node by launching your script directly, then make the scripts executable

        $ chmod u+x scripts/python_node.py
Note: if you want to import the module_to_import.py file from your python_node.py file or from any other file from the package, you'll have to write

        from cpp_python_pkg.module_to_import import....

***1.3 The final ros2 package tree is as shown below***

   After all the modifications, your package tree should look like this.
       
                              └── cpp_python_pkg
                                  ├── CMakeLists.txt 
                                  ├── cpp_python_pkg
                                  │   ├── __init__.py
                                  │   └── module_to_import.py
                                  ├── include
                                  │   └── cpp_python_pkg
                                  │       └── cpp_header.hpp
                                  ├── package.xml
                                  ├── scripts
                                  │   └── python_node.py  
                                  └── src
                                      └── cpp_node.cpp
                                      
The CMakeList.txt and package.xml will be used for both  C++ and python nodes. For the rest, you can see the C++ stuff is clearly separated from python stuff.


**2.0CONFIGURING YOUR ROS2 PACKAGE FOR BOTH C++ AND PYTHON(`package.xml` and `CMakeList.txt`)**

***2.1 Editing the package.eml file***

Now from you terminal navigate to your package folder 

        $ cd ros2_wks/src/cpp_python_pkg
        $ code .

you'll see a bunch of files including package.xml and CMakeList.txt. open package.xml and add the following lines
          
              <buildtool_depend>ament_cmake</buildtool_depend>
              <buildtool_depend>ament_cmake_python</buildtool_depend>
              
by default you should already have a buildtool_depend for ament_cmake since that was asked when creating our standard C++ package from the command line.
here we add another buildtool_depend tag: ament_cmake_python.
in a standard python package, you'd have ament_python, not ament_cmake_python. Make sure not to mix up those two. Using amen_cmake_python means that we will be able to setup our python stuff with cmake, so from the CMakeList.txt file.

              <depend>rclpy</depend>
              <depend>rclcpp</depend>
              
We add a dependency for the ROS2 C++ library (rclcpp) as well as the ROS2 python library(rclpy)

That's all for package.xml.

***2.2 Editing the CMakeLists.txt file***

Here's the complete CMakeLists.txt to install both C++ and python nodes. 
we can split this into 3 parts which are: Dependencies, C++ part and python part

 

       



