#include <string>
#include <unordered_map>

// #include "json.h"
#include "document.h"

// using json = nlohmann::json;

// Need to decide on how to build from current state
// if the current state is stored in JSON files
class Index {
private:
	std::unordered_map<std::string, std::vector<Document*>> index_map;
public:
	Index();
	Index(const std::string& state_file);
	~Index();
	void add_entry(const std::string& word, const Document& document);
	void delete_entry(const std::string& word);
	std::vector<Document>& find_entry(const std::string& word);
	void restore(const std::string& json_filename);
};

