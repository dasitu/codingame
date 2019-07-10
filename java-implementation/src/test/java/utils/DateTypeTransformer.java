package utils;

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

}
