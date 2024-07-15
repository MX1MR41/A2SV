class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [collections.Counter()]
        i = 0

        while i < len(formula):
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                for name, v in top.items():
                    stack[-1][name] += v * multiplier
            else:
                start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                name = formula[start:i]
                start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                stack[-1][name] += count

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))        
