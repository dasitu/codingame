// https://www.codingame.com/ide/puzzle/mayan-calculation

package codingame.medium;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class MayanCalculation {

  private static final int base = 20;

  /**
   * convert Flat Mayan code to int value.
   *
   * @param flatMayanCode flat mayan string, join all rows together
   * @param mayanCodeList full list of code
   * @return corresponding int value of mayan code
   */
  private static int getIntFromFlatMayanCode(
      List<String> flatMayanCode, List<String> mayanCodeList) {
    Collections.reverse(flatMayanCode);
    int intValue = 0;
    for (int i = 0; i < flatMayanCode.size(); i++) {
      intValue += mayanCodeList.indexOf(flatMayanCode.get(i)) * Math.pow(base, i);
    }
    return intValue;
  }

  // convert int value to flat mayan string
  // each mayan number in one list
  private static List<String> getMayanCodeFromDec(long intVar, List<String> mayanCodeList) {
    String twentyFormat = Long.toString(intVar, base);
    List<String> flatMayanCode = new ArrayList<>();
    for (char c : twentyFormat.toCharArray()) {
      int i = Integer.parseInt(String.valueOf(c), base);
      flatMayanCode.add(mayanCodeList.get(i));
    }
    return flatMayanCode;
  }

  // just revert the flat mayan code into original one, rowCount is used as breaker
  private static String revertMayanFormat(List<String> flatMayanCode, int rowCount) {
    List<String> result = new ArrayList<>();
    for (String singleDigit : flatMayanCode) {
      String[] numsLine = singleDigit.split("(?<=\\G.{" + rowCount + "})");
      result.addAll(Arrays.asList(numsLine));
    }
    return String.join(System.lineSeparator(), result);
  }

  // read from system in and format the flat mayan number
  private static List<String> readMayanNumber(Scanner in, int colCount) {
    List<String> flatMayanNumber = new ArrayList<>();
    StringBuilder tempStr = new StringBuilder();
    int s1 = in.nextInt();
    for (int i = 1; i < s1 + 1; i++) {
      tempStr.append(in.next());
      if (i % colCount == 0) {
        flatMayanNumber.add(tempStr.toString());
        tempStr.setLength(0);
      }
    }
    return flatMayanNumber;
  }

  /**
   * read system in and printout the corresponding int value in stdout.
   *
   * @param args nothing needed
   */
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int colCount = in.nextInt();
    int rowCount = in.nextInt();
    List<String> mayanCode = new ArrayList<>(Collections.nCopies(base, ""));
    for (int i = 0; i < rowCount; i++) {
      String line = in.next();
      String[] numsInLine = line.split("(?<=\\G.{" + colCount + "})");
      for (int j = 0; j < numsInLine.length; j++) {
        mayanCode.set(j, mayanCode.get(j) + numsInLine[j]);
      }
    }

    int s1 = getIntFromFlatMayanCode(readMayanNumber(in, colCount), mayanCode);
    int s2 = getIntFromFlatMayanCode(readMayanNumber(in, colCount), mayanCode);

    String operation = in.next();
    long result = 0;
    switch (operation) {
      case "+":
        result = s1 + s2;
        break;
      case "-":
        result = s1 - s2;
        break;
      case "*":
        result = (long) s1 * s2;
        break;
      case "/":
        result = s1 / s2;
        break;
      default:
    }
    System.out.println(revertMayanFormat(getMayanCodeFromDec(result, mayanCode), rowCount));
  }
}
