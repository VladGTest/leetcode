import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] findWords(String[] words) {
        List<String> findWords = new ArrayList<String>();
        List<String> needAlphabet = new ArrayList<String>();
        needAlphabet.add("qwertyuiop");
        needAlphabet.add("asdfghjkl");
        needAlphabet.add("zxcvbnm");
       
        for(int i = 0; i < words.length; i++) {
            if (words[i].isEmpty()) continue;
            
            char tmpChar = words[i].toLowerCase().charAt(0);
            int index = -1;
            boolean isFine = true;

            for(int j = 0; j < needAlphabet.size(); j++) {
                if(needAlphabet.get(j).indexOf(tmpChar) != -1) {
                   index = j;
                   break;
                }
            }
         
            if (index == -1) continue;
            
            for(int j = 1; j < words[i].length(); j++) {
                if(needAlphabet.get(index).indexOf(words[i].toLowerCase().charAt(j)) == -1) {
                    isFine = false;
                    break;
                }
            }
            
            if(isFine) {
                findWords.add(words[i]);
            }
        }
        
        return findWords.toArray(new String[0]);
    }
}