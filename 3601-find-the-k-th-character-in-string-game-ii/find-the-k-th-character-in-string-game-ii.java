class Solution {
    public char kthCharacter(long k, int[] operations) {


        // Store the length of the pattern after each operation
        long[] lengths = new long[operations.length + 1];
        lengths[0] = 1; // Initial pattern is "a"

        // Precompute lengths to avoid building actual strings
        for (int i = 0; i < operations.length; i++) {
            if (operations[i] == 0) {
                lengths[i + 1] = lengths[i] * 2;
            } else {
                lengths[i + 1] = lengths[i] * 2;
            }

            // Edge case: prevent overflow (cut if length exceeds k)
            if (lengths[i + 1] > k) {
                lengths[i + 1] = k;
            }
        }

        int shift = 0; // Tracks the number of +1 shifts
        int index = operations.length;

        // Work backwards to find the original character at position k
        while (index > 0) {
            if (operations[index - 1] == 0) {
                if (k > lengths[index - 1]) {
                    k -= lengths[index - 1]; // It came from duplicated second half
                }
                // Else, it came from the first half — no change to k
            } else {
                if (k > lengths[index - 1]) {
                    k -= lengths[index - 1]; // It came from modified second half
                    shift++; // Since it’s a +1 shift
                } else {
                    // It came from unmodified first half
                }
            }
            index--;
        }

        // The base pattern is "a", so apply final shift to it
        char result = (char) ((('a' - 'a' + shift) % 26 + 'a'));
        return result;

        // String pattern = "a";
        // int index = (int) k;

        // for (int i = 0; i < operations.length; i++) {
        //     if (operations[i] == 0) {
        //         pattern += pattern;

        //     } else {

        //         String newP = "";
        //         for (int j = 0; j < pattern.length(); j++) {
        //             char ch = pattern.charAt(j);
        //             char nextChar = (char) ((ch - 'a' + 1) % 26 + 'a');
        //             newP += nextChar;
        //         }
        //         pattern += newP;
        //     }
        // }

        // return pattern.charAt(index-1);
    }
}