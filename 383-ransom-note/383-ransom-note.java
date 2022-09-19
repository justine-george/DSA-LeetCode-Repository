// class Solution {
//     public boolean canConstruct(String ransomNote, String magazine) {
//         Map<String, Integer> letterCount = new HashMap<>();
        
//         // form letter count map from magazine
//         for (char c: magazine.toCharArray()) {
//             if (letterCount.containsKey(c + ""))
//                 letterCount.put(c + "", letterCount.get(c + "") + 1);
//             else
//                 letterCount.put(c + "", 1);
//         }
        
//         // check whether ransomNote can be made using magazine letters
//         for (char c: ransomNote.toCharArray()) {
//             if (!letterCount.containsKey(c + ""))
//                 return false;
//             else {
//                 if (letterCount.get(c + "") > 0)
//                     letterCount.put(c + "", letterCount.get(c + "") - 1);
//                 else
//                     return false;
//             }
//         }
//         return true;
//     }
// }

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {        
        for (char c: ransomNote.toCharArray()) {
            int index = magazine.indexOf(c);
            
            if (index == -1)
                return false;
            
            magazine = magazine.substring(0, index) + magazine.substring(index + 1);
            
        }
        return true;
    }
}