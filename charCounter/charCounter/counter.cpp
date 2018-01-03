#include "stdafx.h"
#include "counter.h"
#include <fstream>
#include <string>
counter::counter(char* source)
{
	this->source = source;
	for (int i = 0; i <= 127; i++) {
		table[i] = 0;
	}
}
counter::~counter()
{
	delete table;
	delete source;
}
void counter::count()
{
	std::string fileSource = "input/";
	fileSource += source;
	std::ifstream file(fileSource, std::ios::in);
	if (file.is_open()) {
		while (file.good()) {
			input = file.get();
			table[(int)input]++;
		}
	}
	file.close();
}
void counter::saveToFile() 
{
	std::string output="output/";
	output.append(source);
		
	std::ofstream outFile(output, std::ios::out);
	for (int i = 32; i < 127; i++) {
		outFile << (char)i << " --> " << table[i] << std::endl;
	}	
}
void counter::operate() 
{
	count();
	saveToFile();
}
