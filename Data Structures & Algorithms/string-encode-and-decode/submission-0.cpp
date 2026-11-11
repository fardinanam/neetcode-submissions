class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";

        for (string str : strs) {
            encoded += to_string(str.length()) + "#" + str;
        }

        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> decoded;
        // cout << s << endl;

        for (int i = 0; i < s.length();) {
            int j = i;
            
            while(j < s.length() && s[j++] != '#');

            int length = stoi(s.substr(i, j));
            // cout << "found length: " << length << endl;
            // cout << "and str = " << s.substr(j, length) << endl;
            decoded.push_back(s.substr(j, length));

            i = j + length;
        }

        return decoded;
    }
};
