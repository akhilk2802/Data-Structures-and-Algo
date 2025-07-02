class Solution {
    public int distMoney(int money, int children) {

        money -= children;

        if (money < 0) return -1;
        if (money == 0) return 0;

        int cnt7 = money / 7;
        int rem = money % 7;

        if (cnt7 == children && rem == 0) return cnt7;
        if (cnt7 == children - 1 && rem == 3) return cnt7 - 1;

        return Math.min(cnt7, children - 1);
        
    }
}