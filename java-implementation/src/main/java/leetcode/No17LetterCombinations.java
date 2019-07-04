package leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class No17LetterCombinations {

  private HashMap<Integer, String> phoneBoard = new HashMap<>();

  public No17LetterCombinations() {
    int index = 2;
    int letterCount = 3;
    StringBuilder content = new StringBuilder();
    for (char c = 'a'; c <= 'z'; ++c) {
      content.append(c);
      letterCount--;
      if (letterCount == 0) {
        phoneBoard.put(index, content.toString());
        index++;
        content.setLength(0);
        if (index == 7 || index == 9) {
          letterCount = 4;
        } else {
          letterCount = 3;
        }
      }
    }
  }

  public List<String> letterCombinations(String digits) {
    ArrayList<String> answer = new ArrayList<>();

    for (int i = 0; i < digits.length(); i++) {
      char digit = digits.charAt(i);
      String candidates = phoneBoard.get(Character.getNumericValue(digit));

      // initial answer
      if (answer.isEmpty()) {
        for (char candidate : candidates.toCharArray()) {
          answer.add(Character.toString(candidate));
        }
        continue;
      }

      ArrayList<String> newAnswer = new ArrayList<>();
      for (String content : answer) {
        for (char candidate : candidates.toCharArray()) {
          newAnswer.add(content + candidate);
        }
        System.err.println(newAnswer);
      }
      answer = newAnswer;
    }
    return answer;
  }
}
