class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "None"
        return "|?:{}<<<".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        # if not s or s == "|?:{}<<<":
        #     return []
        return s.split("|?:{}<<<")
