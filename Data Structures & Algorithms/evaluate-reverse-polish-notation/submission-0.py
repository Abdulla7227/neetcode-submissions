class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                a = stack.pop()
                b = stack.pop()

                if i == "+":
                    result = b + a
                elif i == "-":
                    result = b - a
                elif i == "*":
                    result = b * a
                else:
                    result = int(b / a)

                stack.append(result)
            else:
                stack.append(int(i))

        return stack[-1]