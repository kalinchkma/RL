#include <iostream>

// override new operator
void *operator new(size_t size) {
  std::cout << "Allocation " << size << "bytes \n";
  return malloc(size);
}

struct Object {
  int x, y, z;
};

int main() {

  std::string s = "Chenobil";
  Object *obj = new Object;
}
