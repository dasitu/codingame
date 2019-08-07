package keng;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public class ListKeng {
  public static void main(String[] args) {
    List<String> immutableList = Arrays.asList("a", "b", "c", "d", "e", "f");
    List<String> mutableList = new ArrayList<>(immutableList);

    // ConcurrentModificationException
//    for (String n: mutableList){
//      mutableList.remove(n);
//      System.out.println(mutableList.toString());
//    }

    // no exception, but not working as expected
    System.out.println(mutableList);
    for (int i = 0; i < mutableList.size(); i++) {
      System.out.println("removing by index:" + i);
      mutableList.remove(i);
      System.out.println(mutableList);
    }

    // reset back to original list
    System.out.println("##########");
    mutableList.clear();
    mutableList.addAll(immutableList);
    // no exception, but not working as expected
    System.out.println(mutableList);
    int originSize = mutableList.size();
    for (int i = 0; i < originSize; i++) {
      System.out.println("removing by index:" + i);
      mutableList.remove(0);
      System.out.println(mutableList);
    }

    // reset back to original list
    System.out.println("##########");
    mutableList.clear();
    mutableList.addAll(immutableList);

    // corrected way with for loop, this is universal for all type
    System.out.println(mutableList);
    for (Iterator<String> iterator = mutableList.iterator(); iterator.hasNext(); ) {
      String element = iterator.next();
      System.out.println("removing:" + element);
      iterator.remove();
      System.out.println(mutableList);
    }
    ;

    // reset back to original list
    System.out.println("##########");
    mutableList.clear();
    mutableList.addAll(immutableList);

    // correct way with while loop, this is universal for all type
    System.out.println(mutableList);
    Iterator<String> iterator = mutableList.iterator();
    while (iterator.hasNext()) {
      String element = iterator.next();
      System.out.println("removing:" + element);
      iterator.remove();
      System.out.println(mutableList);
    }

    // reset back to original list
    System.out.println("##########");
    mutableList.clear();
    mutableList.addAll(immutableList);

    // correct way with ListIterator, this is only for List
    System.out.println(mutableList);
    ListIterator<String> listIterator = mutableList.listIterator();
    while (listIterator.hasNext()) {
      int index = listIterator.nextIndex();
      String element = listIterator.next();
      System.out.printf("removing [%d]: %s \n", index, element);
      listIterator.remove();
      System.out.println(mutableList);
    }

    // #2 keng
    int a = 12345;
    int b = 789012;
    long c = 0;
    c = a * b; // result 1150418548 is incorrect as result is overflow int range
    c = (long) a * b; // result 9,740,353,140‬ is correct
    System.out.println(c);
  }
}
