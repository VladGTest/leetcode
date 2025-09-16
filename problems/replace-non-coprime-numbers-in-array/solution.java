class Solution {
    public List<Integer> replaceNonCoprimes(int[] nums) {
        LinkedList<Integer> stack = new LinkedList<>();
        for (int num : nums) {
            stack.addLast(num);
            while (stack.size() >= 2) {
                int last = stack.pollLast();
                int secondLast = stack.pollLast();
                int gcd = gcd(last, secondLast);
                if (gcd > 1) {
                    
                    long lcm = (long) last * secondLast / gcd;
                    
                    stack.addLast((int) lcm);
                } else {
                   
                    stack.addLast(secondLast);
                    stack.addLast(last);
                    break;
                }
            }
        }
        return stack;
    }
    private int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}