from Queues.Queue import Queue


class BSTNode():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def permute(Ar, k, permlist):
    if k >= len(Ar):
        permlist.append(Ar[:])
        return

    for i in range(k, len(Ar)):
        Ar[i], Ar[k] = Ar[k], Ar[i]
        permute(Ar, k + 1, permlist)
        Ar[i], Ar[k] = Ar[k], Ar[i]


def level_order(node):
    if node == None:
        return [[]]

    result = []

    delimiterNode = BSTNode()

    queue = Queue()
    queue.enqueue(node)
    queue.enqueue(delimiterNode)

    result.append([node.data])

    currentLevelNodes = []
    while queue.size > 0:

        current = queue.dequeue().data

        if queue.size == 0:
            return result

        if current == delimiterNode:
            result.append(currentLevelNodes)
            currentLevelNodes = []
            queue.enqueue(delimiterNode)
            continue

        if current.left != None:
            queue.enqueue(current.left)
            currentLevelNodes.append(current.left.data)
        if current.right != None:
            queue.enqueue(current.right)
            currentLevelNodes.append(current.right.data)


def get_bst_sequences(node):
    bst_sequences = []

    if node == None:
        bst_sequences.append([])
        return bst_sequences

    bst_sequences.append([[]])

    # Iterate over all the levels
    # for each level generate all possible permutations

    # for each bst_sequences
    # for each permutation
    # -->append permutation to the end of bst_sequence.


    levelLists = level_order(node)
    print levelLists
    for levelOrderDataList in levelLists:

        possible_permutations = []
        permute(levelOrderDataList,0,possible_permutations)

        new_bst_sequences = []
        for bst_sequence in bst_sequences:  # [1]

            for permutation in possible_permutations:  # [ [2, 3], [3, 2] ]
                new_bst_sequences.append(bst_sequence + permutation)

        bst_sequences = new_bst_sequences  # [ [1, 2, 3], [1, 3, 2] ]

    for bst_sequence in bst_sequences:
        print bst_sequence
    return bst_sequences


fifty = BSTNode(50)
twenty = BSTNode(20)
sixty = BSTNode(60)
ten = BSTNode(10)
twentyfive = BSTNode(25)
seventy = BSTNode(70)
five = BSTNode(5)
fifteen = BSTNode(15)
sixtyfive = BSTNode(65)
eighty = BSTNode(80)

fifty.left = twenty
fifty.right = sixty

twenty.left = ten
twenty.right = twentyfive

sixty.right = seventy

ten.left = five
ten.right = fifteen

seventy.left = sixtyfive
seventy.right = eighty



result = get_bst_sequences(fifty)

print len(result)


