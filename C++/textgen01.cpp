#include <bits/stdc++.h>

using namespace std;

const string ALPHABETS("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
default_random_engine rand_engine;
uniform_int_distribution<size_t> dist(0, ALPHABETS.length() - 1);

string make_word(int how_long) {
    string word;
    for (int i = 0; i < how_long; ++i) {
        word += ALPHABETS[dist(rand_engine)];
    }            
    return word;
}

unordered_set<string> load_words(string filename, int word_length) {
    unordered_set<string> words;
    ifstream sowpods(filename);
    string word;
    while (sowpods >> word) {
        if (word.length() == word_length) {
            words.insert(word);
        }
    } 
    return words;
}

int main(int argc, char* argv[]) {
    int word_length = stoi(argv[1]);
    unordered_set<string> words = load_words("sowpods.txt", word_length);
    
    int attempt = 0;
    string word;
    while (words.find(word = make_word(word_length)) == words.end()) {
        attempt++;
    }

    cout << word << setw(10) << attempt << endl;
    return 0;
}

