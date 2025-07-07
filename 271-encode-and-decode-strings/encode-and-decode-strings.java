public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder result = new StringBuilder();
        for (String s : strs) {
            result.append(s.length()).append("#").append(s);
        }
        return result.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        int i = 0;

        while (i < s.length()) {
            int j = s.indexOf('#', i); // Find the next separator
            int length = Integer.parseInt(s.substring(i, j)); // Extract length
            String str = s.substring(j + 1, j + 1 + length); // Extract the string
            result.add(str);
            i = j + 1 + length; // Move to the next encoded string
        }

        return result;
    }
}