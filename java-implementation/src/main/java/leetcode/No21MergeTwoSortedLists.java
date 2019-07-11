package leetcode;

import leetcode.dataTypes.ListNode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class No21MergeTwoSortedLists {
  public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

    List<Integer> mergedList = new ArrayList<>();
    ListNode dummyRoot = new ListNode(0);
    ListNode currentNode = dummyRoot;

    dummyRoot.next = l1;
    while (currentNode.next != null){
      currentNode = currentNode.next;
      mergedList.add(currentNode.val);
    }

    dummyRoot.next = l2;
    currentNode = dummyRoot;
    while (currentNode.next != null){
      currentNode = currentNode.next;
      mergedList.add(currentNode.val);
    }

    Collections.sort(mergedList);
    dummyRoot = new ListNode(0);
    ListNode rt = dummyRoot;
    for (Integer v: mergedList){
      rt.next = new ListNode(v);
      rt = rt.next;
    }
    return dummyRoot.next;
  }
}
