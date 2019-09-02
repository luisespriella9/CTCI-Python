#Test Remove Dups

Correct
---------------------------------
#Test return Kth to last

Correct
Correct
Correct
---------------------------------
#Test delete middle node

current list:  0->1->2->3->4->5->6->None
delete middle node:  0->1->2->4->5->6->None
delete middle node:  0->1->4->5->6->None
delete middle node:  0->1->5->6->None
delete middle node:  0->5->6->None
delete middle node:  0->6->None
delete middle node:  0->6->None
current list:  a->b->c->d->e->f->None
delete middle node:  a->b->d->e->f->None
---------------------------------
#Test partition

current list:  3->5->8->5->10->2->1->None
partition around 5:  3->2->1->5->8->5->10->None
---------------------------------
#Test Sum Lists

7->1->6
+
5->9->2
=
2->1->9->None : 912
---------
2->1->0->1
+
5->9->2
=
7->0->3->1->None : 1307