class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(oc,cc,curr):
            if oc==cc==n:
                result.append("".join(curr))
                return

            if oc < n:
                curr.append('(')
                generate(oc+1,cc,curr)
                curr.pop()

            if cc < oc:
                curr.append(')')
                generate(oc,cc+1,curr)
                curr.pop()
        generate(0,0,[])
        return result