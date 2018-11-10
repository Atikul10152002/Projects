#pragma once
#include <iostream>
#include "dep2.cpp"

void dep1() {
	std::cout << "dep1" << std::endl;
	dep2();
}
