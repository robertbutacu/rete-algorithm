(deffacts facts
    (some men evil)
    (all men mortal)
)


(defrule r1 "All A are Bs, all Bs are Cs => All As are Cs"
  (all ?a ?b)
  (all ?b ?c)
  =>
  (assert (all ?a ?c))
  (printout "All " ?a "are " ?b)
  (printout "All " ?b "are " ?c)
  (printout "==>")
  (printout "All " ?a "are " ?c)
)


(defrule r2 "All As are Bs, some As are Cs => All Cs are Bs"
  (all ?a ?b)
  (some ?a ?c)
  =>
  (assert (all ?c ?b))
  (printout "All " ?a "are " ?b)
  (printout "Some" ?a "are" ?c)
  (printout "==>")
  (printout "All " ?c "are " ?b)
)

(defrule r3 "All As are Bs, no Cs are Bs => No Cs are As"
  (all ?a ?b)
  (none  ?c ?b)
  =>
  (assert (none ?c ?a))
  (printout "All" ?a "are" ?b)
  (printout "No" ?c "are'" ?b)
  (printout "==>")
  (printout "No" ?c "are" ?a)
)

