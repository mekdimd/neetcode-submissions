class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();

        // count each word
        for (String s : strs) {    

            // count each char
            int[] count = new int[26];
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                count[c - 'a']++;
            }

            // Insert to result
            String key = Arrays.toString(count);
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(s);
        }

        // return groupings
        return new ArrayList<>(res.values());  
    }
}
