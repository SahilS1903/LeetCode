class Solution {
    public int characterReplacement(String s, int k) {
        int i = 0;
        int max = 0;
        int maxFreq = 0;

        Map<Character, Integer> freq = new HashMap<>();

        for (int j = 0; j < s.length(); j++) {
            char right = s.charAt(j);

            freq.put(right, freq.getOrDefault(right, 0) + 1);

            maxFreq = Math.max(maxFreq, freq.get(right));

            while (j - i + 1 - maxFreq > k) {
                char left = s.charAt(i);

                freq.put(left, freq.get(left) - 1);

                if (freq.get(left) == 0) {
                    freq.remove(left);
                }

                i++;
            }

            max = Math.max(max, j - i + 1);
        }

        return max;
    }
}