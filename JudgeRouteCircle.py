'''
Created on Jul 30, 2018
https://leetcode.com/problems/judge-route-circle/description/
@author: anurag varma
'''
def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    d= {'R' : 0, 'L':0, 'U':0, 'D' : 0}
    for i in range(len(moves)):
        if moves[i] == 'R':
            d['R'] += 1
        elif moves[i] == 'L':
            d['L'] += 1
        elif moves[i] == 'U':
            d['U'] += 1
        elif moves[i] == 'D':
            d['D'] += 1
    print(d)
    
    if d['R'] == d['L'] and d['U'] == d['D']:
        return True
    return False
    
    
moves="LL"

print(judgeCircle(moves))
'''
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
        return count.get('L')  == count.get('R') and count.get('U') == count.get('D')

        record = {}
        for move in moves:
            record[move] = record.get(move, 0) + 1
        return record.get('U', 0) == record.get('D', 0) and record.get('L', 0) == record.get('R', 0)
'''