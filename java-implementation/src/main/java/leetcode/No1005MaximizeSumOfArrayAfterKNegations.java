package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class No1005MaximizeSumOfArrayAfterKNegations {
  public int largestSumAfterKNegations(int[] A, int K) {
    int rtSum = 0;
    Arrays.sort(A);

    List<Integer> positives = new ArrayList<>();
    List<Integer> negatives = new ArrayList<>();

    int firstPosIndex = 0;
    int negSum = 0;
    int posSum = 0;
    for (int i = 0; i < A.length; i++) {
      int v = A[i];
      if (v < 0) {
        negatives.add(v);
        negSum += v;
      } else {
        firstPosIndex = i;
        break;
      }
    }

    for (int i = firstPosIndex; i < A.length; i++) {
      positives.add(A[i]);
      posSum += A[i];
    }


    if (K <= negatives.size()) {
      for (int i = 0; i < K; i++) {
        rtSum += negatives.get(i) * -1;
      }
      for (int i = K; i < negatives.size(); i++) {
        rtSum += negatives.get(i);
      }
      rtSum += posSum;
    } else {
      int leftCount = K - negatives.size();
      if (leftCount % 2 == 0) {
        rtSum = negSum * -1 + posSum;
      } else {
        int minPos = Integer.MAX_VALUE;
        ;
        int minNeg = Integer.MAX_VALUE;
        ;
        if (positives.size() != 0) {
          minPos = positives.get(0);
        }
        if (negatives.size() != 0) {
          minNeg = negatives.get(negatives.size() - 1) * -1;
        }
        int left = minPos < minNeg ? minPos : minNeg;
        rtSum = (negSum * -1) + posSum - (left * 2);
      }
    }
    return rtSum;
  }
}
