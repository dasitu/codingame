package leetcode;

import leetcode.dataTypes.ListNode;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static utils.DateTypeTransformer.arrayToListNode;
import static utils.DateTypeTransformer.listNodeToList;

public class No21MergeTwoSortedListsTest {
  private No21MergeTwoSortedLists testObject = new No21MergeTwoSortedLists();

  @Test
  public void example() {
    int[] inputValues1 = {1, 2, 4};
    int[] inputValues2 = {1, 3, 4};
    int[] answerValues = {1, 1, 2, 3, 4, 4};
    ListNode input1 = arrayToListNode(inputValues1);
    ListNode input2 = arrayToListNode(inputValues2);
    ListNode answer = arrayToListNode(answerValues);

    assertEquals(listNodeToList(answer), listNodeToList(testObject.mergeTwoLists(input1, input2)));
  }
}
