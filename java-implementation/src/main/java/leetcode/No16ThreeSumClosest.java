package leetcode;

import java.util.Arrays;

public class No16ThreeSumClosest {

  public int threeSumClosest(int[] nums, int target) {

    Arrays.sort(nums);
    int answer = 0;
    int minDiff = Integer.MAX_VALUE;

    for (int i = 0; i < nums.length; i++) {
      int leftIndex = i + 1;
      int rightIndex = nums.length - 1;

      while (leftIndex < rightIndex) {
        int currentSum = nums[i] + nums[leftIndex] + nums[rightIndex];
        int diff = currentSum - target;

        if (Math.abs(diff) < Math.abs(minDiff)) {
          answer = currentSum;
          minDiff = diff;
        }

        if (diff > 0) {
          rightIndex--;
        } else {
          leftIndex++;
        }
      }
    }
    return answer;
  }
}
