def iteration(openedBox, queue, boxes, n):
    """
        iteration - The function to while loop
        openedBox:
        queue :
        boxes:

    """
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key < n and not openedBox[key]:
                openedBox[key] = True
                queue.append(key)
                
    result = all(openedBox)
    return result

def canUnlockAll(boxes):
    """
        to implement the unblock app
    """
    n = len(boxes)
    openedBox = [False] * n
    openedBox[0] = True
    queue = [0]

    val = iteration(openedBox, queue, boxes, n)

    return val
