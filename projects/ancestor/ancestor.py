def earliest_ancestor(ancestors, starting_node):
    # start a queue and add starting node
    q = []
    q.append(starting_node)
    # initialize store of earliest ancestors
    anc_list = [starting_node]
    # while queue is not empty
    while len(q) > 0:
        # dequeue first child
        cur_anc = q.pop(0)
        # ancestor is smallest number in ancestor list if ancestor list is not empty
        if len(anc_list) > 0:
            ancestor = min(anc_list)
        # clear anc_list for new loop through ancestors/family connections list
        anc_list = []
        # loop through list of family connections
        for tup in ancestors:
            # if cur_anc is a child (i.e. second element of tuple)
            if cur_anc == tup[1]:
                # append the parent of the child to queue and anc_list
                q.append(tup[0])
                anc_list.append(tup[0])
    # if ancestor is the same as start node, return -1 due to no parents
    if ancestor == starting_node:
        return -1
    # else return ancestor
    else:
        return ancestor

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (11, 8),
             (4, 5), (4, 8), (8, 9), (10, 1)]
print(earliest_ancestor(ancestors, 9))