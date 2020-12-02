#include <string>

class Config {
private:
	int percent_keywords;
	int max_pages;
	int max_ngram_size;

public:
	Config(const std::string& filename);
};