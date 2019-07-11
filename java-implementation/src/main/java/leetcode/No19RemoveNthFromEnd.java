package leetcode;

import java.util.ArrayList;
import java.util.List;

import leetcode.dataTypes.ListNode;

public class No19RemoveNthFromEnd {

  public ListNode removeNthFromEndWithList(ListNode head, int n) {
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

  public ListNode removeNthFromEnd(ListNode head, int n) {

    ListNode dummy = new ListNode(0);
    dummy.next = head;
    int length  = 0;
    ListNode currentNode = head;
    while (currentNode != null) {
      length++;
      currentNode = currentNode.next;
    }
    length -= n;
    currentNode = dummy;
    while (length > 0) {
      length--;
      currentNode = currentNode.next;
    }
    currentNode.next = currentNode.next.next;
    return dummy.next;
  }
}
