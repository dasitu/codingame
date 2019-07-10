package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class No18FourSum {

  /** https://leetcode.com/problems/4sum/
   * @param nums int array, all int candidates
   * @param target int, you should find 4 elements from nums array and the total equals to target
   * @return answer for this puzzle
   */
  public List<List<Integer>> fourSum(int[] nums, int target) {

    Arrays.sort(nums);
    List<List<Integer>> answer = new ArrayList<>();

    for (int outerLeft = 0; outerLeft < nums.length; outerLeft++) {
      for (int outerRight = nums.length - 1; outerRight > 0; outerRight--) {

        int innerLeft = outerLeft + 1;
        int innerRight = outerRight - 1;

        while (innerLeft < innerRight) {
          int currentSum = nums[outerRight] + nums[outerLeft] + nums[innerLeft] + nums[innerRight];

          List<Integer> found = Arrays.asList(
                  nums[outerRight], nums[outerLeft],
                  nums[innerLeft], nums[innerRight]);
          Collections.sort(found);

          if (currentSum == target) {
            if (!isExist(found, answer)) { // avoid duplicate
              answer.add(found);
            }
            innerLeft++;
          } else if (currentSum < target) {
            innerLeft++;
          } else {
            innerRight--;
          }
        }
      }
    }
    return answer;
  }

  private boolean isExist(List<Integer> num, List<List<Integer>> target) {
    for (List<Integer> line : target) {
      //Collections.sort(line);
      if (line.equals(num)) {
        return true;
      }
    }
    return false;
  }
}
