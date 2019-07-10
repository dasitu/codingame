package leetcode;

import leetcode.dataTypes.ListNode;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static utils.DateTypeTransformer.ArrayToListNode;
import static utils.DateTypeTransformer.listNodeToList;

public class No19RemoveNthFromEndTest {
  private No19RemoveNthFromEnd testObject = new No19RemoveNthFromEnd();

  @Test
  public void example() {
    int[] inputValues = {1, 2, 3, 4, 5};
    int nthNode = 2;
    int[] answerValues = {1, 2, 3, 5};
    ListNode input = ArrayToListNode(inputValues);
    ListNode answer = ArrayToListNode(answerValues);

    assertEquals(listNodeToList(answer), listNodeToList(testObject.removeNthFromEnd(input, nthNode)));
  }
}
