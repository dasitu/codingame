package leetcode;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class No20ValidParentheses {
  public boolean isValid(String s) {

    Map<Character, Character> parenthesesMatch = new HashMap<>();
    parenthesesMatch.put('}', '{');
    parenthesesMatch.put(']', '[');
    parenthesesMatch.put(')', '(');

    Stack<Character> stack = new Stack<>();
    for (char c : s.toCharArray()) {
      if (parenthesesMatch.containsKey(c) && stack.size() > 0 && parenthesesMatch.get(c) == stack.peek()) {
        stack.pop();
      }else{
        stack.push(c);
      }
    }

    return stack.isEmpty();
  }
}
