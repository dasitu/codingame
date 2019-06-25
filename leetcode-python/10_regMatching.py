def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    import re
    pattern = p.replace('.', '[a-z]')
    matched = re.search(pattern, s)
    if matched is not None:
        if matched[0] == s:
            return True
    return False

def main():
    testcases = [('aa','a'), ('aa','a*'), ('ab','.*'), ('aab', 'c*a*b'),('mississippi', 'mis*is*p*.')]
    for s, n in testcases:
        return_str = isMatch(s,n)
        print("{}".format(return_str))

main()