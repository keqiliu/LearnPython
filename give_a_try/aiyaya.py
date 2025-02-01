def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """

    if not heights:
        return 0

    stack = []
    ans = 0
    i = 0
    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            idx = stack.pop()
            last_h = heights[idx]
            if not stack:
                width = i
            else:
                width = i - 1 - stack[-1]
            area = last_h * width
            ans = max(ans, area)

    while stack:
        idx = stack.pop()
        last_h = heights[idx]
        if not stack:
            width = i
        else:
            width = i - 1 - stack[-1]
        area = last_h * width
        ans = max(ans, area)

    return ans


print(largestRectangleArea([2,1,2]))