// charCounter.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include "charCounter.h"
#include "counter.h"
int main(int argc, char* argv[]) {
	counter *count = new counter(argv[1]);
	count->operate();
	return 0;
}