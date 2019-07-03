package leetcode;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class No16ThreeSumClosestTest {

  private final No16ThreeSumClosest no16ThreeSumClosest = new No16ThreeSumClosest();

  @Test
  public void example(){
    int[] nums = {-1, 2, 1, -4};
    int target = 1;
    int answer = 2;
    assertEquals(answer, no16ThreeSumClosest.threeSumClosest(nums, target));
  }
}
