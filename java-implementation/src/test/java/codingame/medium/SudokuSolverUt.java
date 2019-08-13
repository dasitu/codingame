package codingame.medium;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static codingame.medium.SudokuSolver.calculateNextPos;
import static codingame.medium.SudokuSolver.getAllBlockTopLeftPos;
import static org.junit.jupiter.api.Assertions.*;

class SudokuSolverUt {

  private SudokuSolver testObject;

  private SudokuSolverUt() {
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
    testObject = new SudokuSolver(convertSudokuStr2List(input));
  }

  private List<List<Integer>> convertSudokuStr2List(String[] sudokuString) {
    List<List<Integer>> puzzleList = new ArrayList<>();
    for (String lineStr : sudokuString) {
      List<Integer> lineArr = new ArrayList<>();
      for (char c : lineStr.toCharArray()) {
        lineArr.add(Integer.parseInt(String.valueOf(c)));
      }
      puzzleList.add(lineArr);
    }
    return puzzleList;
  }

  @Test
  void testGetBlockCandidateMapIndexes() {
    List<Integer> indexes = testObject.getBlockCandidateMapIndexes(3, 4);
    List<Integer> expect = Arrays.asList(30, 31, 32, 39, 40, 41, 48, 49, 50);
    assertEquals(indexes, expect);
  }

  @Test
  void testGetColValues() {
    List<Integer> indexes = testObject.getColValues(3);
    List<Integer> expect = Arrays.asList(0, 6, 0, 0, 0, 1, 0, 5, 0);
    assertEquals(expect, indexes);
  }

  @Test
  void testGetAllBlockTopLeftPos() {
    List<List<Integer>> allBlockTopLeftPos = getAllBlockTopLeftPos();
    List<List<Integer>> expect = new ArrayList<>();
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        expect.add(Arrays.asList(i * 3, j * 3));
      }
    }
    System.out.println("Expected:" + expect.toString());
    assertEquals(expect, allBlockTopLeftPos);
  }

  @Test
  void testCalculateNextPos() {
    List<List<Integer>> poss =
        Arrays.asList(
            Arrays.asList(0, 0), Arrays.asList(0, 8), Arrays.asList(7, 8), Arrays.asList(8, 8));
    List<List<Integer>> expects =
        Arrays.asList(Arrays.asList(0, 1), Arrays.asList(1, 0), Arrays.asList(8, 0), null);
    for (int i = 0; i < poss.size(); i++) {
      assertIterableEquals(
          expects.get(i), calculateNextPos(poss.get(i).get(0), poss.get(i).get(1)));
    }
  }

  @Test
  void testIsFinalAnswerFalse() {
    String[] input = {
      "120070560",
      "507932080",
      "000001000",
      "010240050",
      "308000402",
      "070085010",
      "000700000",
      "080423701",
      "034010028",
    };
    boolean expected = false;
    assertEquals(expected, testObject.isFinalAnswer(convertSudokuStr2List(input)));
  }

  @Test
  void testIsFinalAnswerTrue() {
    String[] input = {
      "123874569",
      "567932184",
      "849651237",
      "916247853",
      "358196472",
      "472385916",
      "291768345",
      "685423791",
      "734519628",
    };
    boolean expected = true;
    assertEquals(expected, testObject.isFinalAnswer(convertSudokuStr2List(input)));
  }
}
