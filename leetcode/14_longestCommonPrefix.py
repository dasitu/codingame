def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    import re
    strs_len = len(strs)
    if strs_len < 1:
        return ""

    shortest_word = strs[0]
    for word in strs:
        if len(word) < len(shortest_word):
            shortest_word = word

    common_prefix = shortest_word
    while len(common_prefix) > 0:
        matched = 0
        for input_str in strs:
            if re.search(r'^' + common_prefix, input_str):
                matched += 1
        if matched == strs_len:
            return common_prefix
        else:
            common_prefix = common_prefix[:-1]
    return ""


testcases = [["flower","flow","flight"], [], ["ca", "a"]]
for strs in testcases:
    print(longestCommonPrefix(strs))
