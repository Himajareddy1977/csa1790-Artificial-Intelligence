premise(p).
premise(q).
premise(r).
conclusion(p,q).
conclusion(q,r).
valid_argument(premise(A), conclusion(A,B)) :- premise(A), conclusion(A,B).
valid_argument(premise(A), conclusion(B,C)) :- valid_argument(premise(A), conclusion(B,C)), premise(A), conclusion(B,C).