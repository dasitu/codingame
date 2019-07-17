// https://www.codingame.com/ide/puzzle/sudoku-solver

package codingame.medium;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class SudokuSolver {

  private int boardWidth = 9;
  private int boardHeight = 9;
  private Map<Integer, List<Integer>> candidateMap = new HashMap<>();
  private List<List<Integer>> sudokuBoard;

  public static void main(String[] args) {

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
    for (int i = 0; i < boardHeight * boardWidth; i++) {
      candidateMap.put(i, new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9)));
    }
    sudokuBoard = puzzle;
    refreshCandidateMap();
    printBoardAndCandidatesHtmlFile();
  }

  public List<List<Integer>> resolveSudoku() {

    // fill with only one candidate
    for (int i = 0; i < 9; i++) {
      updateBoardForSingleCandidate();
    }
    updateCandidateMapForPairByCol();
    updateCandidateMapForPairByRow();

    for (int i = 0; i < 5; i++) {
      updateBoardForSingleCandidate();
    }

    printBoardAndCandidatesHtmlFile();
    return sudokuBoard;
  }


  private void updateBoardForSingleCandidate() {
    for (Integer candidateMapIndex : candidateMap.keySet()) {
      List<Integer> candidates = candidateMap.get(candidateMapIndex);
      if (candidates.size() == 1) {
        int[] pos = calculatePosFromCandidateMapIndex(candidateMapIndex);
        sudokuBoard.get(pos[0]).set(pos[1], candidates.get(0));
      }
    }
    refreshCandidateMap();
  }

  private void updateCandidateMapForPairByCol() {
    for (int col = 0; col < boardWidth; col++) {
      List<Integer> colCandidateMapIndexes = getColCandidateMapIndexes(col);
      updateCandidateMapForPair(colCandidateMapIndexes);
    }
  }

  private void updateCandidateMapForPairByRow() {
    for (int row = 0; row < boardHeight; row++) {
      List<Integer> colCandidateMapIndexes = getRowCandidateMapIndexes(row);
      updateCandidateMapForPair(colCandidateMapIndexes);
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
            commonCandidatesMap.put(candidate, new ArrayList<>(
                    Arrays.asList(rowOrColCandidateMapIndexes.get(i), index))
            );
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

    String htmlFilePath = "target/classes/sudokuBoard.html";

    try {
      FileWriter htmlBoardWriter = new FileWriter(htmlFilePath);
      String head = "<!DOCTYPE html>\n"
              + "<html lang=\"en\">\n"
              + "<head>\n"
              + "<link rel=\"stylesheet\" type=\"text/css\" href=\"sudokuTable.css\">\n"
              + "</head>"
              + "<body>"
              + "<div class=\"main\"><table>";
      String tail = "</div></table>\n</body>\n</html>";
      htmlBoardWriter.write(head);
      for (int row = 0; row < sudokuBoard.size(); row++) {
        htmlBoardWriter.write("<tr>");
        List<Integer> line = sudokuBoard.get(row);
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
    int candidateIndex = row * boardWidth + col;
    return candidateMap.get(candidateIndex);
  }

  private String getCandidateTableHtml(List<Integer> candidates) {
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
        candidateTable.append("<td>" + printValue + "</td>");
      }
      candidateTable.append("</tr>\n");
    }
    candidateTable.append("</table></div>");
    return candidateTable.toString();
  }

  List<Integer> getColValues(int col) {
    List<Integer> colValues = new ArrayList<>();
    for (List<Integer> line : sudokuBoard) {
      for (int colIndex = 0; colIndex < line.size(); colIndex++) {
        if (colIndex == col) {
          colValues.add(line.get(colIndex));
        }
      }
    }
    return colValues;
  }

  List<Integer> getBlockCandidateMapIndexes(int row, int col) {
    int[] topLeft = calculateBlockFirstPos(row, col);
    int startPosMapIndex = calculateCandidateMapIndex(topLeft[0], topLeft[1]);
    List<Integer> blockCandidateMapIndexes = new ArrayList<>();
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        blockCandidateMapIndexes.add(startPosMapIndex + i * boardWidth + j);
      }
    }
    return blockCandidateMapIndexes;
  }

  private List<Integer> getColCandidateMapIndexes(int col) {
    List<Integer> colCandidateMapIndexes = new ArrayList<>();
    for (int i = 0; i < boardHeight; i++) {
      int colIndex = i * boardWidth + col;
      colCandidateMapIndexes.add(colIndex);
    }
    return colCandidateMapIndexes;
  }

  private List<Integer> getRowCandidateMapIndexes(int row) {
    List<Integer> rowCandidateMapIndexes = new ArrayList<>();
    for (int i = 0; i < boardHeight; i++) {
      int rowIndex = boardWidth * row + i;
      rowCandidateMapIndexes.add(rowIndex);
    }
    return rowCandidateMapIndexes;
  }

  private int[] calculatePosFromCandidateMapIndex(int candidateMapIndex) {
    int[] pos = new int[2];
    pos[0] = candidateMapIndex / boardWidth;
    pos[1] = candidateMapIndex % boardWidth;
    return pos;
  }

  private int calculateCandidateMapIndex(int row, int col) {
    return row * boardWidth + col;
  }

  private int[] calculateBlockFirstPos(int row, int col) {
    int[] topLeft = new int[2];
    topLeft[0] = (row / 3) * 3;
    topLeft[1] = (col / 3) * 3;
    return topLeft;
  }

  private List<Integer> getBlockValues(int row, int col) {
    int[] topLeft = calculateBlockFirstPos(row, col);
    List<Integer> blockValues = new ArrayList<>();
    for (int rowIndex = topLeft[0]; rowIndex < topLeft[0] + 3; rowIndex++) {
      for (int colIndex = topLeft[1]; colIndex < topLeft[1] + 3; colIndex++) {
        blockValues.add(sudokuBoard.get(rowIndex).get(colIndex));
      }
    }
    return blockValues;
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
