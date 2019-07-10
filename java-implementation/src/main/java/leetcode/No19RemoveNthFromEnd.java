package leetcode;

import java.util.ArrayList;
import java.util.List;

import leetcode.dataTypes.ListNode;

public class No19RemoveNthFromEnd {

  public ListNode removeNthFromEnd(ListNode head, int n) {
    List<Integer> mapOfListNode = new ArrayList<>();
    mapOfListNode.add(head.val);

    while (head.next != null) {
      head = head.next;
      mapOfListNode.add(head.val);
    }

    int removalIndex = mapOfListNode.size() - n;
    mapOfListNode.remove(removalIndex);

    // restore to NodeList structure
    ListNode dummyRoot = new ListNode(0);
    ListNode ptr = dummyRoot;
    for (Integer value : mapOfListNode) {
      ptr.next = new ListNode(value);
      ptr = ptr.next;
    }
    return dummyRoot.next;
  }
}
