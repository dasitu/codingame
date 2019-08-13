// https://www.codingame.com/ide/puzzle/sudoku-solver

package codingame.medium;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class SudokuSolver {

  private Map<Integer, List<Integer>> candidateMap = new HashMap<>();
  private List<List<Integer>> sudokuBoard;

  public static void main(String[] args) throws InterruptedException {

    List<List<Integer>> puzzle = new ArrayList<>();
    Scanner in = new Scanner(System.in);
    for (int i = 0; i < 9; i++) {
      String lineStr = in.nextLine();
      List<Integer> lineArr = new ArrayList<>();
      for (char c : lineStr.toCharArray()) {
        lineArr.add(Integer.parseInt(String.valueOf(c)));
      }
      puzzle.add(lineArr);
    }

    SudokuSolver sudokuSolver = new SudokuSolver(puzzle);
    List<List<Integer>> answer = sudokuSolver.resolveSudoku();
    for (List<Integer> line : answer) {
      StringBuilder lineStr = new StringBuilder();
      for (Integer c : line) {
        lineStr.append(c);
      }
      System.out.println(lineStr.toString());
    }
  }

  SudokuSolver(List<List<Integer>> puzzle) {

    // initial the candidateMap with all possibilities
    // index represent the position in the sudoku table
    // continues index from 0 to 81
    for (int i = 0; i < 9 * 9; i++) {
      candidateMap.put(i, new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9)));
    }
    sudokuBoard = puzzle;
    refreshCandidateMap();
    printBoardAndCandidatesHtmlFile();
  }

  public List<List<Integer>> resolveSudoku() throws InterruptedException {
    //resolveSudokuByRules();
    resolveSudokuByRecursion(0, 0, sudokuBoard);
    printBoardAndCandidatesHtmlFile("java-implementation/target/classes/answer.html", sudokuBoard);
    return sudokuBoard;
  }

  private boolean isRowValid(int row, List<List<Integer>> puzzle) {
    return isUnitValid(puzzle.get(row), puzzle);
  }

  private boolean isColValid(int col, List<List<Integer>> puzzle) {
    return isUnitValid(getColValues(col, puzzle), puzzle);
  }

  private boolean isBlockValid(int row, int col, List<List<Integer>> puzzle) {
    return isUnitValid(getBlockValues(row, col, puzzle), puzzle);
  }

  private boolean isUnitValid(List<Integer> unitValues, List<List<Integer>> puzzle) {
    List<Integer> values = new ArrayList<>(unitValues);
    values.removeIf(n -> n == 0);
    Set<Integer> hashSet = new LinkedHashSet<>(values);
    return hashSet.size() == values.size();
  }

  boolean isFinalAnswer(List<List<Integer>> puzzle) {
    // check whether found the final answer
    List<Integer> expectedList = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);

    // check row
    int rowMatchedCount = 9;
    for (int rowIndex = 0; rowIndex < 9; rowIndex++) {
      List<Integer> rowNums = new ArrayList<>(puzzle.get(rowIndex));
      Collections.sort(rowNums);
      if (rowNums.equals(expectedList)) {
        rowMatchedCount -= 1;
      }
    }

    // check col
    int colMatchedCount = 9;
    for (int colIndex = 0; colIndex < 9; colIndex++) {
      List<Integer> colNums = new ArrayList<>(getColValues(colIndex, puzzle));
      Collections.sort(colNums);
      if (colNums.equals(expectedList)) {
        colMatchedCount -= 1;
      }
    }

    // check block
    int blockMatchedCount = 9;
    for (List<Integer> rowAndCol : getAllBlockTopLeftPos()) {
      List<Integer> blockNums =
          new ArrayList<>(getBlockValues(rowAndCol.get(0), rowAndCol.get(1), puzzle));
      Collections.sort(blockNums);
      if (blockNums.equals(expectedList)) {
        blockMatchedCount -= 1;
      }
    }

    return (rowMatchedCount + colMatchedCount + blockMatchedCount) == 0;
  }

  private Boolean resolveSudokuByRecursion(int row, int col, List<List<Integer>> puzzle) throws InterruptedException {
    //printBoardAndCandidatesHtmlFile("java-implementation/target/classes/sudokuTempBoard.html", puzzle);
    //TimeUnit.SECONDS.sleep(1);
    List<List<Integer>> mirrorBoard = new ArrayList<>();
    for (List<Integer> rowValues: puzzle){
      List<Integer> mirrorRow = new ArrayList<>(rowValues);
      mirrorBoard.add(mirrorRow);
    }
    if (isFinalAnswer(puzzle)) {
      sudokuBoard = puzzle;
      return true;
    }

    if (puzzle.get(row).get(col) != 0) {
      List<Integer> next = getNextEmptyPos(row, col, mirrorBoard);
      if (next != null) {
        row = next.get(0);
        col = next.get(1);
      } else {
        return true;
      }
    }

    // get the next index
    int nextRow;
    int nextCol;
    List<Integer> next = getNextEmptyPos(row, col, mirrorBoard);
    if (next != null) {
      nextRow = next.get(0);
      nextCol = next.get(1);
    } else {
      nextRow = row;
      nextCol = col;
    }

    List<Integer> candidates = getCandidate(row, col);
    for (Integer candidate : candidates) {
      mirrorBoard.get(row).set(col, candidate);
      if (!isRowValid(row, mirrorBoard)
          || !isColValid(col, mirrorBoard)
          || !isBlockValid(row, col, mirrorBoard)) {
        continue;
      }
      boolean found = resolveSudokuByRecursion(nextRow, nextCol, mirrorBoard);
      if (found) {
        return true;
      }
    }
    return false;
  }

  private void resolveSudokuByRules() {
    // fill with only one candidate
    for (int i = 0; i < 9; i++) {
      updateBoardForSingleCandidate();
    }
    updateCandidateMapForPairByCol();
    updateCandidateMapForPairByRow();

    for (int i = 0; i < 5; i++) {
      updateBoardForSingleCandidate();
    }

    updateBoardForSinglePossibilityByBlock();
    updateBoardForSinglePossibilityByRow();
    updateBoardForSinglePossibilityByCol();
    refreshCandidateMap();

    for (int i = 0; i < 5; i++) {
      updateBoardForSingleCandidate();
    }

    printBoardAndCandidatesHtmlFile();
  }

  private void updateBoardForSinglePossibilityByRow() {
    for (int row = 0; row < 9; row++) {
      List<Integer> rowCandidateMapIndexes = getRowCandidateMapIndexes(row);
      updateBoardForSinglePossibility(rowCandidateMapIndexes);
    }
  }

  private void updateBoardForSinglePossibilityByCol() {
    for (int col = 0; col < 9; col++) {
      List<Integer> colCandidateMapIndexes = getColCandidateMapIndexes(col);
      updateBoardForSinglePossibility(colCandidateMapIndexes);
    }
  }

  private void updateBoardForSinglePossibilityByBlock() {
    for (List<Integer> pos : getAllBlockTopLeftPos()) {
      List<Integer> colCandidateMapIndexes = getBlockCandidateMapIndexes(pos.get(0), pos.get(1));
      updateBoardForSinglePossibility(colCandidateMapIndexes);
    }
  }

  private void updateBoardForSinglePossibility(List<Integer> candidateMapIndexes) {
    for (Integer candidateMapIndex : candidateMapIndexes) {
      List<Integer> candidates = candidateMap.get(candidateMapIndex);
      if (candidates == null) {
        continue;
      }
      for (Integer candidate : candidates) {
        boolean isUnique = true;
        for (Integer otherCandidateMapIndex : candidateMapIndexes) {
          if (otherCandidateMapIndex.equals(candidateMapIndex)) {
            continue;
          }
          if (!candidateMap.containsKey(otherCandidateMapIndex)) {
            continue;
          }
          if (candidateMap.get(otherCandidateMapIndex).contains(candidate)) {
            isUnique = false;
            break;
          }
        }
        if (isUnique) {
          setSudokuBoardByCandidateMapIndex(candidateMapIndex, candidate);
        }
      }
    }
  }

  private void updateBoardForSingleCandidate() {
    for (Integer candidateMapIndex : candidateMap.keySet()) {
      List<Integer> candidates = candidateMap.get(candidateMapIndex);
      if (candidates.size() == 1) {
        setSudokuBoardByCandidateMapIndex(candidateMapIndex, candidates.get(0));
      }
    }
    refreshCandidateMap();
  }

  private void updateCandidateMapForPairByCol() {
    for (int col = 0; col < 9; col++) {
      List<Integer> colCandidateMapIndexes = getColCandidateMapIndexes(col);
      updateCandidateMapForPair(colCandidateMapIndexes);
    }
  }

  private void updateCandidateMapForPairByRow() {
    for (int row = 0; row < 9; row++) {
      List<Integer> rowCandidateMapIndexes = getRowCandidateMapIndexes(row);
      updateCandidateMapForPair(rowCandidateMapIndexes);
    }
  }

  private void updateCandidateMapForPair(List<Integer> rowOrColCandidateMapIndexes) {
    Map<List<Integer>, List<Integer>> commonCandidatesMap = new HashMap<>();
    for (int i = 0; i < rowOrColCandidateMapIndexes.size() - 1; i++) {
      List<Integer> candidate = candidateMap.get(rowOrColCandidateMapIndexes.get(i));
      if (candidate == null) {
        continue;
      }
      for (int j = i + 1; j < rowOrColCandidateMapIndexes.size(); j++) {
        Integer index = rowOrColCandidateMapIndexes.get(j);
        if (candidate.equals(candidateMap.get(index))) {
          if (commonCandidatesMap.containsKey(candidate)) {
            commonCandidatesMap.get(candidate).add(index);
          } else {
            commonCandidatesMap.put(
                candidate,
                new ArrayList<>(Arrays.asList(rowOrColCandidateMapIndexes.get(i), index)));
          }
        }
      }
    }

    // commonCandidates found
    if (commonCandidatesMap.size() != 0) {
      // validate whether these commons are valid
      // candidates should be equal with indexes count, then this is pair situation
      Iterator<List<Integer>> iterator = commonCandidatesMap.keySet().iterator();
      while (iterator.hasNext()) {
        List<Integer> candidate = iterator.next();
        List<Integer> candidateIndexes = commonCandidatesMap.get(candidate);
        if (candidate.size() != candidateIndexes.size()) {
          iterator.remove();
        }
      }
    }

    // validation is passed, still have commons
    // start to update the candidateMap
    if (commonCandidatesMap.size() != 0) {
      for (List<Integer> commonCandidate : commonCandidatesMap.keySet()) {
        List<Integer> commonCandidateIndexes = commonCandidatesMap.get(commonCandidate);
        for (Integer common : commonCandidate) {
          for (Integer index : rowOrColCandidateMapIndexes) {
            if (candidateMap.get(index) == null) {
              continue;
            }
            if (candidateMap.get(index).contains(common)
                && !commonCandidateIndexes.contains(index)) {
              candidateMap.get(index).remove(common);
            }
          }
        }
      }
    }
    refreshCandidateMap();
  }

  private void printBoardAndCandidatesHtmlFile() {
    //String cwd = System.getProperty("user.dir");
    //System.out.println("Current working directory : " + cwd);
    printBoardAndCandidatesHtmlFile("java-implementation/target/classes/sudokuBoard.html", sudokuBoard);
  }

  private void printBoardAndCandidatesHtmlFile(String htmlFilePath, List<List<Integer>> board) {
    try {
      FileWriter htmlBoardWriter = new FileWriter(htmlFilePath);
      String head =
          "<!DOCTYPE html>\n"
              + "<html lang=\"en\">\n"
              + "<head>\n"
              + "<link rel=\"stylesheet\" type=\"text/css\" href=\"sudokuTable.css\">\n"
              + "</head>"
              + "<body>"
              + "<div class=\"main\"><table>";
      String tail = "</div></table>\n</body>\n</html>";
      htmlBoardWriter.write(head);
      for (int row = 0; row < board.size(); row++) {
        htmlBoardWriter.write("<tr>");
        List<Integer> line = board.get(row);
        for (int col = 0; col < line.size(); col++) {
          Integer valueInBoard = line.get(col);
          String printContent = String.valueOf(valueInBoard);
          if (valueInBoard == 0) {
            printContent = "\n" + getCandidateTableHtml(getCandidate(row, col)) + "\n";
          }
          htmlBoardWriter.write("<td>" + printContent + "</td>");
        }
        htmlBoardWriter.write("</tr>\n");
      }
      htmlBoardWriter.write(tail);
      htmlBoardWriter.close();
    } catch (IOException fileIoException) {
      System.out.println(fileIoException.getMessage());
    }
  }

  private List<Integer> getCandidate(int row, int col) {
    int candidateIndex = row * 9 + col;
    return candidateMap.get(candidateIndex);
  }

  private static String getCandidateTableHtml(List<Integer> candidates) {
    StringBuilder candidateTable = new StringBuilder("<div class=\"candidate\"><table>\n");
    int currentNode;
    for (int i = 0; i < 3; i++) {
      candidateTable.append("<tr>");
      for (int j = 0; j < 3; j++) {
        currentNode = i * 3 + j + 1;
        String printValue = "&nbsp;&nbsp;";
        if (candidates.contains(currentNode)) {
          printValue = String.valueOf(currentNode);
        }
        candidateTable.append("<td>").append(printValue).append("</td>");
      }
      candidateTable.append("</tr>\n");
    }
    candidateTable.append("</table></div>");
    return candidateTable.toString();
  }

  static List<Integer> getColValues(int col, List<List<Integer>> puzzle) {
    List<Integer> colValues = new ArrayList<>();
    for (List<Integer> line : puzzle) {
      for (int colIndex = 0; colIndex < line.size(); colIndex++) {
        if (colIndex == col) {
          colValues.add(line.get(colIndex));
        }
      }
    }
    return colValues;
  }

  List<Integer> getColValues(int col) {
    return getColValues(col, sudokuBoard);
  }

  static List<List<Integer>> getAllBlockTopLeftPos() {
    List<List<Integer>> allBlockTopLeftPos = new ArrayList<>();
    for (int row = 0; row < 9; row += 3) {
      for (int col = 0; col < 9; col += 3) {
        allBlockTopLeftPos.add(Arrays.asList(row, col));
      }
    }
    return allBlockTopLeftPos;
  }

  List<Integer> getBlockCandidateMapIndexes(int row, int col) {
    int[] topLeft = calculateBlockFirstPos(row, col);
    int startPosMapIndex = calculateCandidateMapIndex(topLeft[0], topLeft[1]);
    List<Integer> blockCandidateMapIndexes = new ArrayList<>();
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        blockCandidateMapIndexes.add(startPosMapIndex + i * 9 + j);
      }
    }
    return blockCandidateMapIndexes;
  }

  private List<Integer> getColCandidateMapIndexes(int col) {
    List<Integer> colCandidateMapIndexes = new ArrayList<>();
    for (int i = 0; i < 9; i++) {
      int colIndex = i * 9 + col;
      colCandidateMapIndexes.add(colIndex);
    }
    return colCandidateMapIndexes;
  }

  private List<Integer> getRowCandidateMapIndexes(int row) {
    List<Integer> rowCandidateMapIndexes = new ArrayList<>();
    for (int i = 0; i < 9; i++) {
      int rowIndex = 9 * row + i;
      rowCandidateMapIndexes.add(rowIndex);
    }
    return rowCandidateMapIndexes;
  }

  private void setSudokuBoardByCandidateMapIndex(int candidateMapIndex, int value) {
    int[] rowAndCol = calculatePosFromCandidateMapIndex(candidateMapIndex);
    sudokuBoard.get(rowAndCol[0]).set(rowAndCol[1], value);
  }

  private static int[] calculatePosFromCandidateMapIndex(int candidateMapIndex) {
    int[] pos = new int[2];
    pos[0] = candidateMapIndex / 9;
    pos[1] = candidateMapIndex % 9;
    return pos;
  }

  static List<Integer> calculateNextPos(int row, int col) {
    List<Integer> nextPos = new ArrayList<>(Arrays.asList(row, col));
    nextPos.set(1, col + 1);
    if (nextPos.get(1) >= 9) {
      if (row + 1 >= 9) {
        return null;
      }
      nextPos.set(0, row + 1);
      nextPos.set(1, 0);
    }
    return nextPos;
  }

  static List<Integer> getNextEmptyPos(int row, int col, List<List<Integer>> puzzle) {
    List<Integer> next = new ArrayList<>();
    while (row < 9 && col < 9) {
      next = calculateNextPos(row, col);
      if (next == null) {
        return null;
      }
      row = next.get(0);
      col = next.get(1);
      if (puzzle.get(row).get(col) == 0) {
        break;
      }
    }
    return next;
  }

  private static int calculateCandidateMapIndex(int row, int col) {
    return row * 9 + col;
  }

  private static int[] calculateBlockFirstPos(int row, int col) {
    int[] topLeft = new int[2];
    topLeft[0] = (row / 3) * 3;
    topLeft[1] = (col / 3) * 3;
    return topLeft;
  }

  private static List<Integer> getBlockValues(int row, int col, List<List<Integer>> puzzle) {
    int[] topLeft = calculateBlockFirstPos(row, col);
    List<Integer> blockValues = new ArrayList<>();
    for (int rowIndex = topLeft[0]; rowIndex < topLeft[0] + 3; rowIndex++) {
      for (int colIndex = topLeft[1]; colIndex < topLeft[1] + 3; colIndex++) {
        blockValues.add(puzzle.get(rowIndex).get(colIndex));
      }
    }
    return blockValues;
  }

  private List<Integer> getBlockValues(int row, int col) {
    return getBlockValues(row, col, sudokuBoard);
  }

  private void refreshCandidateMap() {
    for (int row = 0; row < sudokuBoard.size(); row++) {
      List<Integer> rowValues = sudokuBoard.get(row);
      for (int col = 0; col < rowValues.size(); col++) {
        int candidateMapIndex = calculateCandidateMapIndex(row, col);
        if (rowValues.get(col) != 0) {
          candidateMap.remove(candidateMapIndex);
        } else {
          // refresh according to row
          candidateMap.get(candidateMapIndex).removeIf(rowValues::contains);
          // refresh according to col
          candidateMap.get(candidateMapIndex).removeIf(getColValues(col)::contains);
          // refresh according to block
          candidateMap.get(candidateMapIndex).removeIf(getBlockValues(row, col)::contains);
        }
      }
    }
  }
}