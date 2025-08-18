"""
when will be least number of cycles ?

-when you can execute job in each cycle
-but you can't execute two same jobs in consecutive cycles. Once you execute job X, you need to wait till
time of n seconds before you can come back to this same job.
-You need to do something useful within these n seconds you have.
-You can execute other jobs which are not X.

"""

from collections import deque, Counter, defaultdict
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:

    count = Counter(tasks)
    tasks = []
    for key, count in count.items():
        tasks.append([key, count])

    tasks = sorted(tasks, key=lambda x: x[1], reverse=True)
    q = deque(tasks)
    t = 0
    accessed_hash = defaultdict()
    freq_q = None
    freq_hash = None
    job_hash = None
    job_q = None
    while q or accessed_hash:
        if t in accessed_hash:
            job_hash, freq_hash = accessed_hash[t]
        else:
            if q:
                job_q, freq_q = q.popleft()
            else:
                t += 1
                continue
        if freq_q and freq_hash and freq_q >= freq_hash and job_hash != job_q: # a job in q is having a more frequency. execute job in q
            k = t+1
            while k in accessed_hash:
                k += 1
            freq_q -= 1
            if freq_q > 0:
                accessed_hash[k] = (job_q, freq_q) # reschedule it at later time

            if t in accessed_hash:
                del accessed_hash[t]  # remove the job at this time

        elif freq_q and freq_hash and freq_hash > freq_q and job_hash != job_q: # a hashed job is more freq than q job.
            if t in accessed_hash:
                del accessed_hash[t]  # remove hashed job from q
            freq_hash -= 1  # hash frequency down
            if freq_hash > 0:
                accessed_hash[t + n + 1] = (job_hash, freq_hash) # resechule if freq > 0
            if job_q and freq_q:
                q.appendleft((job_q, freq_q)) # restore back the q job since we did not execute it
        elif freq_q:
            freq_q -= 1
            if freq_q > 0:
                accessed_hash[t + n + 1] = (job_q, freq_q)

        elif freq_hash:
            freq_hash -= 1
            if freq_hash > 0:
                accessed_hash[t + n + 1] = (job_hash, freq_hash)

            if t in accessed_hash:
                del accessed_hash[t]

        t = t + 1

    return t


tasks = ["A","A","A","B","B","B"]
n = 2


tasks = ["A","A","A","B","B","B"]
n = 0


tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

#
#
# tasks = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C']
# n = 2


print(leastInterval(tasks, n))

