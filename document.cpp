#include <vector>

#include "document.h"

Document::Document(unsigned int id, const std::vector<unsigned int>& positions) {
	this->id = id;
	this->positions = new std::vector<unsigned int>();
	for(int i = 0; i < positions.size(); ++i)
		this->positions.push_back(positions[i]);
}


Document::Document(const Document& d) {
	this->id = d->id;
	this->positions = new std::vector<unsigned int>();
	for(unsigned int i = 0; i < d->positions.size(); ++i)
		this->positions.push_back(d->positions[i]);
}


Document::~Document() {
	delete this->positions;
}


unsigned int get_id() {
	return this->id;
}


const std::vector<unsigned int>& get_positions() {
	return this->positions;
}
