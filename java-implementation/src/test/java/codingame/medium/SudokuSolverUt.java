package codingame.medium;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SudokuSolverUt {

  private SudokuSolver testObject;

  private SudokuSolverUt(){
    String[] input = {
            "800000000",
            "003600000",
            "070090200",
            "050007000",
            "000045700",
            "000100030",
            "001000068",
            "008500010",
            "090000400",
    };
    List<List<Integer>> puzzle = new ArrayList<>();
    for (String lineStr: input){
      List<Integer> lineArr = new ArrayList<>();
      for (char c : lineStr.toCharArray()) {
        lineArr.add(Integer.parseInt(String.valueOf(c)));
      }
      puzzle.add(lineArr);
    }
    testObject = new SudokuSolver(puzzle);
  }

  @Test
  void testGetBlockCandidateMapIndexes(){
    List<Integer> indexes = testObject.getBlockCandidateMapIndexes(3, 4);
    List<Integer> expect = Arrays.asList(30, 31, 32, 39, 40, 41, 48, 49, 50);
    assertEquals(indexes, expect);
  }

  @Test
  void testGetColValues(){
    List<Integer> indexes = testObject.getColValues(3);
    List<Integer> expect = Arrays.asList(0,6,0,0,0,1,0,5,0);
    assertEquals(expect, indexes);
  }

}
