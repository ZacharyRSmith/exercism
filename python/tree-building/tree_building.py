class Record():

    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():

    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    # def __str__(self):
    #     return f'self.node_id "{self.node_id}", self.children "{self.children}"'
    # def __unicode__(self):
    # return f'self.node_id "{self.node_id}", self.children "{self.children}"'
    def __repr__(self):
        return f'self.node_id "{self.node_id}"; self.children "{self.children}"'


def validate_records(records):
    ordered_id = [record.record_id for record in records]
    def validate(record):
        if record.record_id == record.parent_id:
            if record.record_id != 0:
                raise ValueError(f'The only node whose parent is itself is the root node, but record "{record}" violates this.')
        elif record.parent_id > record.record_id:
            raise ValueError(f'Each non-root node`s parent_id should be < record_id, but record "{record}" violates this.')

    if records:
        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError(f'The latest record_id should equal (num records - 1) but was "{ordered_id[-1]}".')
        if ordered_id[0] != 0:
            raise ValueError(f'Root node not found.')
    for record in records:
        validate(record)


def BuildTree(records):
    records.sort(key=lambda x: x.record_id)
    validate_records(records)
    trees = [Node(record.record_id) for record in records]
    for record in records[1:]:
        parent = next(tree for tree in trees
                      if tree.node_id == record.parent_id)
        tree = next(tree for tree in trees
                    if tree.node_id == record.record_id)
        child = tree
        parent.children.append(child)
    return trees and trees[0] or None
BuildTree([
    Record(0, 0),
    Record(1, 0),
    Record(2, 0),
    Record(3, 1),
    Record(4, 1),
    Record(5, 1),
    Record(6, 2)
])
