// https://leetcode.com/problems/basic-calculator/

package leetcode;

import java.util.Stack;

public class No224BasicCalculator {

  public int calculate(String s) {
    System.out.println("input:" + s);
    Stack<String> statementStack = new Stack<>();
    String answer = "";
    statementStack.push(answer);
    String cleanStatement = s.replace(" ", "");
    for (char c : cleanStatement.toCharArray()) {
      if (c == '(') {
        statementStack.push("");
      } else if (c == ')') {
        String statement = statementStack.pop();
        int innerValue = calculator(statement);
        String currentStatement = statementStack.pop();

        // handling negative number like -1
        if (innerValue < 0 && !currentStatement.equals("")) {
          innerValue *= -1;
          char lastOperator = currentStatement.charAt(currentStatement.length() - 1);
          currentStatement = currentStatement.substring(0, currentStatement.length() - 1);
          if (lastOperator == '+') {
            currentStatement += '-';
          } else if (lastOperator == '-') {
            currentStatement += '+';
          }
        }

        statementStack.push(currentStatement + innerValue);
      } else {
        statementStack.push(statementStack.pop() + c);
      }
    }
    return calculator(statementStack.pop());
  }

  private int calculator(String s) {
    System.out.print("calculating:" + s);
    s = s + '+'; // add additional operator to trigger calculation
    int answer = 0;
    StringBuilder number = new StringBuilder("0");
    char operator = '+';
    for (char c : s.toCharArray()) {
      if (c == '-' || c == '+' || c == '*' || c == '/') {
        int value = Integer.parseInt(number.toString());
        switch (operator) {
          case '+':
            answer += value;
            break;
          case '-':
            answer -= value;
            break;
          default:
        }
        number.setLength(0); // clean the cumulative number as it has been added to answer.
        operator = c;
      } else {
        number.append(c);
      }
    }
    System.out.println("=" + answer);
    return answer;
  }
}
