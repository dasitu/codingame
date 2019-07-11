package leetcode;

import org.junit.jupiter.api.Test;
import utils.DateTypeTransformer;

import java.util.Collections;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;


public class No18FourSumTest {

  private No18FourSum testObject = new No18FourSum();

  @Test
  public void example(){
    int[] nums = {1, 0, -1, 0, -2, 2};
    int target = 0;
    Integer[][] answer = {
            {-2, -1, 1, 2},
            {-2, 0, 0, 2},
            {-1, 0, 0, 1},
    };
    List<List<Integer>> expect = DateTypeTransformer.twoDArrayToTwoDList(answer);
    List<List<Integer>> output = testObject.fourSum(nums, target);
    assertEquals(expect.size(), output.size());
    assertEquals(expect, output);
  }

  @Test
  public void failed1(){
    int[] nums = {-3,-2,-1,0,0,1,2,3};
    int target = 0;
    Integer[][] answer = {
            {-3,-2,2,3},
            {-3,-1,1,3},
            {-3,0,0,3},
            {-3,0,1,2},
            {-2,-1,0,3},
            {-2,-1,1,2},
            {-2,0,0,2},
            {-1,0,0,1}
    };
    List<List<Integer>> expect = DateTypeTransformer.twoDArrayToTwoDList(answer);
    List<List<Integer>> output = testObject.fourSum(nums, target);
    assertEquals(expect.size(), output.size());
    assertEquals(expect, output);
  }
}
