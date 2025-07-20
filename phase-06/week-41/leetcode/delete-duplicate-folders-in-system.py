class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)

        self.is_deleted = False


class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:

        root = TrieNode()
        for path in paths:
            node = root
            for folder_name in path:
                node = node.children[folder_name]

        structure_map = defaultdict(list)

        def serialize_and_group(node: TrieNode) -> str:

            if not node.children:
                return ""

            structure_parts = []
            for name, child_node in sorted(node.children.items()):
                child_structure = serialize_and_group(child_node)
                structure_parts.append(f"{name}({child_structure})")

            structure_str = "".join(structure_parts)

            if structure_str:
                structure_map[structure_str].append(node)

            return structure_str

        serialize_and_group(root)

        for nodes in structure_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True

        ans = []

        def collect_paths(node: TrieNode, current_path: list[str]):

            for name, child_node in node.children.items():

                if not child_node.is_deleted:

                    new_path = current_path + [name]
                    ans.append(new_path)
                    collect_paths(child_node, new_path)

        collect_paths(root, [])

        return ans
