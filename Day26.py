# 205. Isomorphic Strings

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        s_to_t_mapping = {}
        t_to_s_mapping = {}

        for i in range(len(s)):
            if s[i] in s_to_t_mapping:
                if s_to_t_mapping[s[i]] != t[i]:
                    return False
            else:
                s_to_t_mapping[s[i]] = t[i]

            if t[i] in t_to_s_mapping:
                if t_to_s_mapping[t[i]] != s[i]:
                    return False
            else:
                t_to_s_mapping[t[i]] = s[i]

        return True
