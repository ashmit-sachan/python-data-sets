def IOTBts(root):
    if root is None:
        return []
    return IOTBts(root.left) + [root.key] + IOTBts(root.right)
