class Solution {
    public int findLucky(int[] arr) {

        Map<Integer, Integer> map = new HashMap<>();
        for (int num : arr) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        Arrays.sort(arr);
        for (int i = arr.length - 1; i >= 0; i--) {
            if (map.get(arr[i]) == arr[i]) {
                return arr[i];
            }
        }
        return -1;
    }
}