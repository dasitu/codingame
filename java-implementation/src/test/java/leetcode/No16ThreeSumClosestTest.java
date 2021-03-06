package leetcode;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class No16ThreeSumClosestTest {

  private No16ThreeSumClosest testObject = new No16ThreeSumClosest();

  @Test
  public void example(){
    int[] nums = {-1, 2, 1, -4};
    int target = 1;
    int answer = 2;
    assertEquals(answer, testObject.threeSumClosest(nums, target));
  }
}
