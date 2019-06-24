// https://www.codingame.com/ide/puzzle/organic-compounds
package easy;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class OrganicCompounds {

  private static ArrayList<ArrayList<Integer>> organicCompound = new ArrayList<>();

  public static void main(String[] args) {

    ArrayList<ArrayList<Integer>> compoundPos = new ArrayList<>();

    Scanner in = new Scanner(System.in);
    int N = in.nextInt();
    if (in.hasNextLine()) {
      in.nextLine();
    }
    for (int i = 0; i < N; i++) {
      String compound = in.nextLine();
      ArrayList<Integer> line = new ArrayList<>();
      for (int j = 0; j <= compound.length() - 3;j += 3){
        String cell = compound.substring(j, j+3);
        if (cell.startsWith("CH")) {
          ArrayList<Integer> pos = new ArrayList<>(Arrays.asList(i, j/3));
          compoundPos.add(pos);
        }
        String digOnly = cell.replaceAll("\\D+",""); //Remove all non-digital characters
        if (digOnly.length()==0)
          digOnly = "0";
        line.add(Integer.parseInt(digOnly));
      }
      organicCompound.add(line);
    }

    System.err.println("organicCompound:" + organicCompound);
    System.err.println("compoundPos:" + compoundPos);

    for (ArrayList<Integer> pos : compoundPos){
      if (!isValid(pos)) {
        System.out.println("INVALID");
        return;
      }
    }
    System.out.println("VALID");
  }

  private static Boolean isValid(ArrayList<Integer> pos){

    System.err.println("validating:" + pos);
    // sum of 4 direction should equal to 4
    Integer row = pos.get(0);
    Integer col = pos.get(1);
    Integer selfValue = organicCompound.get(row).get(col);
    Integer upValue, downValue, leftValue, rightValue;
    upValue = downValue = leftValue = rightValue= 0;
    if(row - 1 > 0 && col < organicCompound.get(row - 1).size())
      upValue = organicCompound.get(row - 1).get(col);
    if (row + 1 < organicCompound.size() && col < organicCompound.get(row + 1).size())
      downValue = organicCompound.get(row + 1).get(col);
    if (col - 1 > 0)
      leftValue = organicCompound.get(row).get(col - 1);
    if (col + 1 < organicCompound.get(row).size())
      rightValue = organicCompound.get(row).get(col + 1);

    System.err.println("selfVal:" + selfValue);
    System.err.println("upVal:" + upValue);
    System.err.println("downVal:" + downValue);
    System.err.println("leftVal:" + leftValue);
    System.err.println("rightVal:" + rightValue);

    if ((selfValue + upValue + downValue + leftValue + rightValue) == 4)
      return Boolean.TRUE;

    return Boolean.FALSE;
  }
}

