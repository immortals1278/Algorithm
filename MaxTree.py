class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def construct_maximum_binary_tree(nums): #构造树的方法
    if not nums:
        return None

    max_val = max(nums)
    max_index = nums.index(max_val)

    root = TreeNode(max_val) #将值包装成TreeNode对象赋给root
    root.left = construct_maximum_binary_tree(nums[:max_index]) #切片不写表示尽头，包含左边不包含右边
    root.right = construct_maximum_binary_tree(nums[max_index + 1:])

    return root


def preorder_traversal(root): #展示树的方法
    result = [] #初始化result数组

    def helper(node):
        if node is None:
            return

        result.append(str(node.val)) #该节点不为空就将该节点的值放入result数组

        # 按照根左右的顺序遍历
        if node.left:
            helper(node.left)
        elif node.right:
            result.append("null") #如果左边没节点右边有，就在原本放左节点的位置放一个null

        if node.right:
            helper(node.right)
        elif node.left:
            result.append("null") #同理

    helper(root)
    return " ".join(result) #用空格将 `result` 列表的所有元素连接成一个字符串。


nums = list(map(int, input().split())) #map是迭代器
root = construct_maximum_binary_tree(nums)
print(preorder_traversal(root), end="") #end=“” 输出后不换行