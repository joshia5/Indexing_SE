#include "config.h"
#include <string>
#include <iostream>
#include <fstream>

Config::Config(const std::string& filename) {
	std::ifstream infile("config.ini");
	std::string param;
	int value;
	while(infile >> param >> value) {
		if(param.compare("Pct_Keywords"))
			this->percent_keywords = value;
		if(param.compare("MAX_Pages_queried"))
			this->max_pages = value;
		if(param.compare("MAX_NGram"))
			this->max_ngram_size = value;
	}
}