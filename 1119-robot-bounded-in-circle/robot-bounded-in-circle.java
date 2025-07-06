class Solution {
    public boolean isRobotBounded(String instructions) {

        // Initially facing North (dx = 0, dy = 1)
        int dx = 0, dy = 1;
        int x = 0, y = 0;

        for (char c : instructions.toCharArray()) {
            if (c == 'G') {
                x += dx;
                y += dy;
            } else if (c == 'L') {
                // Turn left: (dx, dy) becomes (-dy, dx)
                int temp = dx;
                dx = -dy;
                dy = temp;
            } else if (c == 'R') {
                // Turn right: (dx, dy) becomes (dy, -dx)
                int temp = dx;
                dx = dy;
                dy = -temp;
            }
        }

        // The robot is bounded if it's back at the origin
        // OR it's not facing North (which means it will loop in a circle eventually)
        return (x == 0 && y == 0) || !(dx == 0 && dy == 1);
    }
}