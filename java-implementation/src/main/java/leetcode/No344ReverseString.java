package leetcode;

public class No344ReverseString {
  public void reverseString(char[] s) {
    char c;
    int len = s.length;
    for (int i = 0; i < len / 2; i++) {
      c = s[i];
      s[i] = s[len - i - 1];
      s[len - 1 - i] = c;
    }
  }
}
