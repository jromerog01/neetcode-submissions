class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> uniques = new HashSet<>();

        for (int x : nums){
            uniques.add(x);
        }

        return nums.length != uniques.size();

    }
}