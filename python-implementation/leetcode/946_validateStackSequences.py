def validateStackSequences(pushed, popped):
    """
    :type pushed: List[int]
    :type popped: List[int]
    :rtype: bool
    """
    stack = [9999]
    pushed.append(9999)
    popped.append(9999)
    for push in pushed:
        while len(stack) != 0 and stack[-1] == popped[0]:
            stack.pop()
            popped.pop(0)
        stack.append(push)
    return stack == [9999]

#pushed = [1, 2, 3, 4, 5]
#popped = [4, 5, 3, 2, 1]

#pushed = [2,1,0]
#popped = [1,2,0]

pushed = [1, 0, 2]
popped = [2, 1, 0]

print(validateStackSequences(pushed, popped))
