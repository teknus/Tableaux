#Pyhton 3
from Tableaux import *

# > implicacao
# !	negacao
# | ou
# & e
#Fomulas Notavel de teste

main_branch = [
			[(-1,"(p|q)"),(1, '(p>(r|s))'),(1, "(q>(r|s))"),(1,"(r>(t|u))"),(1,"(s>(t|u))"),(-1,"(t|u)")],
			[(1,"(l|k)"),(1,"(k>(a|b))"),(1,"(l>(a|b))"),(1, '(a>(c|d))'),(1, "(b>(c|d))"),(1,"(c>(e|f))"),(1,"(d>(e|f))"),(-1,"(e|f)")],
			[(1,"(p|q)"),(1,"(p>(l|k))"),(1,"(q>(l|k))"),(1,"(k>(a|b))"),(1,"(l>(a|b))"),(1, '(a>(c|d))'),(1, "(b>(c|d))"),(1,"(c>(e|f))"),(1,"(d>(e|f))"),(-1,"(e|f)")],
			[(1,"(s|w)"),(1,"(s>(p|q))"),(1,"(w>(p|q))"),(1,"(p>(l|k))"),(1,"(q>(l|k))"),(1,"(k>(a|b))"),(1,"(l>(a|b))"),(1, '(a>(c|d))'),(1, "(b>(c|d))"),(1,"(c>(e|f))"),(1,"(d>(e|f))"),(-1,"(e|f)")],
			[(1,"(m|n)"),(1,"(m>(s|w))"),(1,"(n>(s|w))"),(1,"(s>(p|q))"),(1,"(w>(p|q))"),(1,"(p>(l|k))"),(1,"(q>(l|k))"),(1,"(k>(a|b))"),(1,"(l>(a|b))"),(1, '(a>(c|d))'),(1, "(b>(c|d))"),(1,"(c>(e|f))"),(1,"(d>(e|f))"),(-1,"(e|f)")],
            [(1,"(r|t)"),(1,"(r>(m|n))"),(1,"(t>(m|n))"),(1,"(m>(s|w))"),(1,"(n>(s|w))"),(1,"(s>(p|q))"),(1,"(w>(p|q))"),(1,"(p>(l|k))"),(1,"(q>(l|k))"),(1,"(k>(a|b))"),(1,"(l>(a|b))"),(1, '(a>(c|d))'),(1, "(b>(c|d))"),(1,"(c>(e|f))"),(1,"(d>(e|f))"),(-1,"(e|f)")],
			[(1,'(g|h)'),(1,"(g>(r|t))"),(1,"(h>(r|t))"),(1,"(r>(m|n))"),(1,"(t>(m|n))"),(1,"(m>(s|w))"),(1,"(n>(s|w))"),(1,"(s>(p|q))"),(1,"(w>(p|q))"),(1,"(p>(l|k))"),(1,"(q>(l|k))"),(1,"(k>(a|b))"),(1,"(l>(a|b))"),(1, '(a>(c|d))'),(1, "(b>(c|d))"),(1,"(c>(e|f))"),(1,"(d>(e|f))"),(-1,"(e|f)")],
			[(1,'(z|o)'),(1,'(z>(g|h))'),(1,'(o>(g|h))'),(1,"(g>(r|t))"),(1,"(h>(r|t))"),(1,"(r>(m|n))"),(1,"(t>(m|n))"),(1,"(m>(s|w))"),(1,"(n>(s|w))"),(1,"(s>(p|q))"),(1,"(w>(p|q))"),(1,"(p>(l|k))"),(1,"(q>(l|k))"),(1,"(k>(a|b))"),(1,"(l>(a|b))"),(1, '(a>(c|d))'),(1, "(b>(c|d))"),(1,"(c>(e|f))"),(1,"(d>(e|f))"),(-1,"(e|f)")],
			[(1,"(L|K)"),(1,'(L>(z|o))'),(1,'(K>(z|o))'),(1,'(z>(g|h))'),(1,'(o>(g|h))'),(1,"(g>(r|t))"),(1,"(h>(r|t))"),(1,"(r>(m|n))"),(1,"(t>(m|n))"),(1,"(m>(s|w))"),(1,"(n>(s|w))"),(1,"(s>(p|q))"),(1,"(w>(p|q))"),(1,"(p>(l|k))"),(1,"(q>(l|k))"),(1,"(k>(a|b))"),(1,"(l>(a|b))"),(1, '(a>(c|d))'),(1, "(b>(c|d))"),(1,"(c>(e|f))"),(1,"(d>(e|f))"),(-1,"(e|f)")]
			]

for x in main_branch:
	run(x)

#lista de nos fechados
#Pilha de ramos