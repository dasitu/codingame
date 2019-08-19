// https://leetcode.com/problems/basic-calculator-ii/

package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class No227BasicCalculatorIi {

  public int calculate(String s) {
    System.out.println("227 input:" + s);
    Stack<String> statementStack = new Stack<>();
    String answer = "";
    statementStack.push(answer);
    String cleanStatement = s.replace(" ", "");
    for (char c : cleanStatement.toCharArray()) {
      if (c == '(') {
        statementStack.push("");
      } else if (c == ')') {
        String statement = statementStack.pop();
        int innerValue = calculateSingleStatement(statement);
        String currentStatement = statementStack.pop();

        // handling negative number like -1
        if (innerValue < 0) {
          currentStatement += "(" + innerValue + ")";
        } else {
          currentStatement += innerValue;
        }

        statementStack.push(currentStatement);
      } else {
        statementStack.push(statementStack.pop() + c);
      }
    }
    return calculateSingleStatement(statementStack.pop());
  }

  private int calculateSingleStatement(String s) {
    System.out.print("calculating:" + s);
    List<String> formulaStrList = new ArrayList<>();
    StringBuilder number = new StringBuilder("0");
    boolean appendSymbol = false;
    for (char c : s.toCharArray()) {
      if (!appendSymbol && (c == '-' || c == '+' || c == '*') || c == '/') {
        formulaStrList.add(number.toString());
        formulaStrList.add(String.valueOf(c));
        number.setLength(0); // clean the cumulative number as it has been added to answer.
      } else if (c == '(') {
        appendSymbol = true;
        number.setLength(0);
      } else if (c == ')') {
        appendSymbol = false;
      } else {
        number.append(c);
      }
    }
    if (number.length() != 0) {
      formulaStrList.add(number.toString());
    }
    int answer = calculateRecursive(formulaStrList);
    System.out.println("=" + answer);
    return answer;
  }

  private void doSingleCalculate(List<String> formulaList, String operator) {
    int index = formulaList.indexOf(operator);
    int firstIndex = index - 1;
    int secondIndex = index + 1;
    int firstNum = Integer.parseInt(formulaList.get(firstIndex));
    int secondNum = Integer.parseInt(formulaList.get(secondIndex));
    int result = 0;
    switch (operator) {
      case "+":
        result = firstNum + secondNum;
        break;
      case "-":
        result = firstNum - secondNum;
        break;
      case "*":
        result = firstNum * secondNum;
        break;
      case "/":
        result = firstNum / secondNum;
        break;
    }
    formulaList.set(index, String.valueOf(result));
    formulaList.remove(firstIndex);
    formulaList.remove(secondIndex - 1); // after firstIndex is removed, the second index is changed
  }

  private int calculateRecursive(List<String> formulaList) {
    if (formulaList.size() == 1) {
      return Integer.parseInt(formulaList.get(0));
    }

    List<String> operators = Arrays.asList("*/", "+-");
    for (String operator : operators) {
      String op =
          formulaList.stream()
              .filter(
                  e ->
                      e.equals(String.valueOf(operator.charAt(0)))
                          || e.equals(String.valueOf(operator.charAt(1))))
              .findFirst()
              .orElse(null);
      if (op != null) {
        doSingleCalculate(formulaList, op);
        calculateRecursive(formulaList);
      }
    }

    return Integer.parseInt(formulaList.get(0));
  }
}
