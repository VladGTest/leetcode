class Solution {
    public List<String> removeAnagrams(String[] words) {
        List<String> result = new ArrayList<>();
        result.add(words[0]);
        for (int i = 1; i < words.length; i++) {
            if (isNotAnagram(words[i - 1], words[i])) {
                result.add(words[i]);
            }
        }
        return result;
    }

     private boolean isNotAnagram(String firstWord, String secondWord) {
        if (firstWord.length() != secondWord.length()) {
            return true;
        }
        int[] characterCount = new int[26];
        for (int i = 0; i < firstWord.length(); i++) {
            characterCount[firstWord.charAt(i) - 'a']++;
        }
        for (int i = 0; i < secondWord.length(); i++) {
            if (--characterCount[secondWord.charAt(i) - 'a'] < 0) {
                return true;
            }
        }
        return false;

    }
}