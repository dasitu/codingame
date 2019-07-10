package utils;

import leetcode.dataTypes.ListNode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class DateTypeTransformer {

  public static <T> List<List<T>> twoDArrayToTwoDList(T[][] twoDArray) {
    List<List<T>> twoDList = new ArrayList<>();
    for (T[] array : twoDArray) {
      twoDList.add(Arrays.asList(array));
    }
    return twoDList;
  }

  public static ListNode ArrayToListNode(int[] nodeValues) {
    ListNode dummyRoot = new ListNode(0);
    ListNode ptr = dummyRoot;
    for (int item : nodeValues) {
      ptr.next = new ListNode(item);
      ptr = ptr.next;
    }
    return dummyRoot.next;
  }

  public static List<Integer> listNodeToList(ListNode listNode) {
    List<Integer> listValue = new ArrayList<>();
    listValue.add(listNode.val);
    while (listNode.next != null) {
      listNode = listNode.next;
      listValue.add(listNode.val);
    }
    return listValue;
  }

}
