// class Solution {
//     public long calculateScore(String[] instructions, int[] values) {

//         Set<String> seen = new HashSet<>();
//         long score = 0;

//         int i = 0;

//         while ( i < instructions.length){
//             if (instructions[i].equals("add") && !seen.contains(instructions[i])){
//                 score = score + values[i];
//                 seen.add(instructions[i]);
//                 i++;
//             }
//             if (instructions[i].equals("jump") && !seen.contains(instructions[i])) {
//                 seen.add(instructions[i]);
//                 i = i + values[i];
//             }
//         }
//         return score;
//     }
// }

class Solution {
    public long calculateScore(String[] instructions, int[] values) {

        Set<Integer> seen = new HashSet<>();
        long score = 0;

        int i = 0;

        while (i < instructions.length) {
            if (seen.contains(i)) {
                break;
            }
            seen.add(i);

            if (instructions[i].equals("add")) {
                score += values[i];
                i++;
            } else if (instructions[i].equals("jump")) {
                int jump = values[i];
                i += jump;

                // Exit if jump takes us out of bounds
                if (i < 0 || i >= instructions.length) {
                    break;
                }
            } else {
                i++;
            }
        }
        return score;
    }
}