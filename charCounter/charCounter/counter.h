#pragma once
#include <fstream>	// file operations
#include <string>	// char -> string
class counter
{
private:
	int table[127];
	int size;
	char input;
	char* source;

	void count();
	void saveToFile();
public:
	counter(char* source);
	void operate();
	~counter();
};

