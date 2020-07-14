"""Greedy-Sig builds a binary heap for a sequence x = x1, . . . , xn by sequentially adding xi as
a child to the the tree Ti−1 built in the previous iteration, if such an addition is feasible. The
greedy insertion rule is to add xi
into the slot with the largest value smaller than or equal to xi
. To
support efficient updates, Greedy-Sig also maintains the signature of the tree, sig(Ti), where each
element in the signature points to its associated slot in Ti
. Insertion of xi therefore corresponds
to first identifying the predecessor, pred(xi), in sig(Ti−1) (if it does not exist, the sequence is not
heapable). Next, xi
is inserted into the corresponding slot in Ti−1, coupled with deleting pred(xi)
from sig(Ti−1), and inserting two copies of xi
, the slots for xi
’s children. Greedy-Sig starts with
the tree T1 = x1 and iterates until it exhausts x (in which case it returns T = Tn) or finds that
the sequence is not heapable. Standard dictionary data structures supporting pred, insert and
delete require O(log n) time per operation, but we can replace each number with its rank in the
sequence, and use van Emde Boas trees [9] to index the signatures, yielding an improved bound of
O(log log n) time per operation, albeit in the word ram model."""
import itertools

def greedonlyseq(seq):
    sig=[seq[0],seq[0]]
    for i in range(1,len(seq)):
      value=seq[i]
      bottom = 0
      top = len(sig)-1
      while(top>bottom+1):
        mid = (top + bottom) // 2
        if(sig[mid]>=value):
          bottom=mid
        else:
          top = mid

      if(sig[bottom]>value):
        bottom+=1
      if(sig[bottom]>value):
        return "No heap"
      sig=sig[0:bottom]+[value,value]+sig[bottom+1:]
    return sig

x=list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
count = 0
for i in x:
  if (i[0]==1 and greedonlyseq(i) != "No heap"):
    #print(i)
    count+=1
print(count)


