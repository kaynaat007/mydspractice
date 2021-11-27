"""
Easy problem.
Trivial
"""


def truncateSentence(s: str, k: int) -> str:

    return ' '.join(s.split(' ')[:k])

s = 'Hello how are you Contestant'
k = 4

s = 'What is the solution to this problem'
k = 4

s = 'chopper is not a tanuki'
k = 5
print(truncateSentence(s, k))