package leetcode;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class No17LetterCombinationsTest {

  private No17LetterCombinations no17LetterCombinations = new No17LetterCombinations();

  @Test
  public void example(){
    String digits = "23";
    ArrayList<String> answer = new ArrayList<>(Arrays.asList("ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"));
    assertEquals(answer, no17LetterCombinations.letterCombinations(digits));
  }
}

