#include <unordered_map>
#include <string>

#include "index.h"
#include "document.h"


Index::Index() {
	this->index = new std::unordered_map<std::string, std::vector<Document*>>();
}


Index::Index(const std::string& state_file) {

}


Index::~Index() {

}


void add_entry(const std::string& word, const Document& document) {
	// check if word is in index

	// add word and document

}


void delete_entry(const std::string& word) {
	// check if word is in index

	// delete word and free associated Document

}


std::vector<Document>& find_entry(const std::string& word) {
	// check if word is in index

	// copy contents and return

}


void restore(const std::string& json_filename) {
	// reset index from JSON file
	
}
