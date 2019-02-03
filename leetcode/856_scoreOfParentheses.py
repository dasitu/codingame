class Solution:

    @staticmethod
    def find_closing_parenthesis(text, start_index):
        end_index = start_index
        counter = 1
        while counter > 0:
            end_index += 1
            c = text[end_index]
            if c == '(':
                counter += 1
            elif c == ')':
                counter -= 1
        return end_index

    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        cur_index = 0
        total = 0
        while cur_index < len(S):
            closing_index = self.find_closing_parenthesis(S, cur_index)
            start_index = cur_index + 1
            inside = S[start_index:closing_index]
            if inside != "":
                total += 2 * (self.scoreOfParentheses(inside))
            else:
                total += 1
            cur_index = closing_index + 1

        return total


testcases = ["(()(()))", "()", "(())", "()()"]
solution = Solution()
for S in testcases:
    print(solution.scoreOfParentheses(S))
