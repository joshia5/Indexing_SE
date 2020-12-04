#include <vector>

class Document {
private:
	unsigned int id;
	std::vector<unsigned int> positions;
public:
	Document(unsigned int id, std::vector<unsigned int> positions);
	Document(const Document& d);
	~Document();

	unsigned int get_id();
	const std::vector<unsigned int>& get_positions();
};
