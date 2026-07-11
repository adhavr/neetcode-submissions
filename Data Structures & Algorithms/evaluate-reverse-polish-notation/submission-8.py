class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token == "+":
                s.append(s.pop() + s.pop())
            elif token == "-":
                s.append((s.pop() - s.pop())*-1)
            elif token == "*":
                s.append(s.pop() * s.pop())
            elif token == "/":
                x = s.pop()
                y = s.pop()
                s.append(int(float(y) / x))
            else:
                s.append(int(token))
        return s[0]
