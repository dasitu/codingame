package leetcode;

import leetcode.dataTypes.ListNode;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static utils.DateTypeTransformer.arrayToListNode;
import static utils.DateTypeTransformer.listNodeToList;

public class No1005MaximizeSumOfArrayAfterKNegationsTest {

  private No1005MaximizeSumOfArrayAfterKNegations testObject = new No1005MaximizeSumOfArrayAfterKNegations();

  @Test
  public void example1() {
    int[] input1 = {4, 2, 3};
    int input2 = 1;
    int answer = 5;
    assertEquals(answer, testObject.largestSumAfterKNegations(input1, input2));
  }

  @Test
  public void example2() {
    int[] input1 = {3,-1,0,2};
    int input2 = 3;
    int answer = 6;
    assertEquals(answer, testObject.largestSumAfterKNegations(input1, input2));
  }

  @Test
  public void example3() {
    int[] input1 = {2,-3,-1,5,-4};
    int input2 = 2;
    int answer = 13;
    assertEquals(answer, testObject.largestSumAfterKNegations(input1, input2));
  }

  @Test
  public void failed1() {
    int[] input1 = {-8,3,-5,-3,-5,-2};
    int input2 = 6;
    int answer = 22;
    assertEquals(answer, testObject.largestSumAfterKNegations(input1, input2));
  }

}
