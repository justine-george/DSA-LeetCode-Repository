class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        x = self.par[x]
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        
        # make disjoint set
        # map { email: idx of account }
        email_account_map = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_account_map:
                    # these 2 indexes should be merged, 
                    # since they have a common email
                    uf.union(i, email_account_map[email])
                else:
                    email_account_map[email] = i
        
        print(email_account_map)
        # { account: [...emails]}
        email_group = defaultdict(list)
        for e, i in email_account_map.items():
            leader = uf.find(i)
            email_group[leader].append(e)

        res = []
        for ac_idx, emails in email_group.items():
            res.append([accounts[ac_idx][0]] + sorted(emails))
        return res