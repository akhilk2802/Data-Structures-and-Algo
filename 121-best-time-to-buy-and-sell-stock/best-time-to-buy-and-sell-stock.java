class Solution {
    public int maxProfit(int[] prices) {
        
        int profit = 0;
        int lowestPrice = Integer.MAX_VALUE;

        for (int price : prices){
            if (price < lowestPrice){
                lowestPrice = price;
            }
            profit = Math.max(profit, price - lowestPrice);
            
        }
        
        return profit;

    }
}