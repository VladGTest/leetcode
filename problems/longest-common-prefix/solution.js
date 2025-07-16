/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let strWord = strs[0];

    for(let i = 0; i < strWord.length;i++){
        for(let j = 0; j < strs.length;j++){
            if(strWord[i] != strs[j][i]){
                return strWord.slice(0, i);
            }
        }
    }

    return strWord;
    
};