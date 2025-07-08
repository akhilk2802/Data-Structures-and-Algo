class SnapshotArray {

    List<List<int[]>> records = new ArrayList<>();
    int snap_id;

    public SnapshotArray(int length) {
        for (int i = 0; i < length; i++) {
            records.add(new ArrayList<>());
        }
        snap_id = 0;
    }

    public void set(int index, int val) {
        List<int[]> arr = records.get(index);
        if (!arr.isEmpty() && arr.get(arr.size() - 1)[0] == snap_id) {
            arr.get(arr.size() - 1)[1] = val; // overwrite last value for same snap_id
        } else {
            arr.add(new int[]{snap_id, val});
        }
    }

    public int snap() {
        return snap_id++;
    }

    public int get(int index, int snap_id) {
        List<int[]> arr = records.get(index);
        if (arr.isEmpty()) return 0;

        int left = 0, right = arr.size() - 1;
        int res = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr.get(mid)[0] <= snap_id) {
                res = arr.get(mid)[1];
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
    }
}