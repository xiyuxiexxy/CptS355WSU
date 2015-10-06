(*	cpts355 ml project	*)
(*	xiyu xie 		*)



(*	in_list ('a, 'a list)		*)

fun	in_list ( a, []) 	= false	
| 	in_list ( a,(x::xs)) 	= if a= x 
					then true 
				  else 
					in_list (a,xs)


(*	intersection ('a list,'a list)	*)

fun 	intersection ([],l)	= []
|	intersection ((x::xs),l)= if in_list(x,xs) 
				  	then intersection(xs,l)
				  else 
					if in_list (x,l)
						then x::intersection(xs,l)
					else 	
						intersection(xs,l)

(* 	filter fn list	*)	

fun 	filter pre l 	= 
let
	fun	f ([], result )	  	= rev result
	|	f ((x::xs), result) 	= if pre x 
						then f (xs, x:: result)
					  else
						 f (xs, result)
in f (l, [])
end


(*    quicksort fn(x,y) list		*)


fun 	quicksort pred []  = []
|	quicksort pred [x] = [x]
| 	quicksort pred (x::xs) = 
let
	val (trueList, falseList) =
 	let 
		fun partition l =
		let 
			fun	loop ([],trueList,falseList)    = (rev trueList, rev falseList) 
 			|	loop (h::t,trueList, falseList) = 
								   if pred (h,x) 
									then loop (t,h::trueList,falseList)
 								   else 
									loop (t, trueList,h::falseList)
 			in loop (l,[],[])
			end
	in partition xs
	end
in 	quicksort pred trueList @ (x:: (quicksort pred falseList))
end



(*	datatype either, datatype eitherTree *)


datatype either		= STRING of string |INT of int
datatype eitherTree	= LEAF of either | NODE of eitherTree*eitherTree



(*	eitherSearch eitherTree int 	*)


fun 	eitherSearch (LEAF (INT x))       n	=  x=n
|	eitherSearch (LEAF (STRING s))    n	=  false
|	eitherSearch (NODE (left, right)) n 	=  eitherSearch left n orelse (eitherSearch right n)



(*	eitherTest	*)
fun eitherTest ()	=
let
	val L11 = LEAF (INT 1)
	val L2a = NODE (L11, LEAF (STRING "a"))
	val L1b = LEAF (STRING "B")
	val L2b = NODE (LEAF (INT 3), L1b)
	val L2c	= NODE (LEAF (INT 4), LEAF (INT 5))
	val L2d = NODE (LEAF (STRING "abcd"), LEAF (STRING "dcba"))
	val L3c = NODE (L2c, L2d)
	val L3a = NODE (L2a, LEAF (INT 2))
	val L3b = NODE (LEAF (STRING "C"), L2b)
	val L4 = NODE (L3a,L3b)
	val L5 = NODE(L4, L3c)

in	if (( eitherSearch L5 3) =true ) andalso (eitherSearch L5 7) =false then true
	else false
end




(*	 6.treeToString		*)

datatype 'a Tree = LEAF of 'a | NODE of ('a Tree) list

fun  	treeToString f (LEAF s) = f s 
|	treeToString f (NODE l) = 
	let 
		fun applyf l = treeToString f l
	in "(" ^ (String.concat (map applyf l)) ^")"
	end 





(*	7.permutation	*)


fun	perms [] = [[]]
| 	perms (x::xs) = 
	let 
		fun insert x [] = [[x]]
		|   insert x (y::ys) =  
		let 
			fun cosy l = y::l
		in	(x::y::ys)::( map cosy (insert x ys ))
		end

		fun insertx l = insert x l

	in	List.concat( List.map insertx (perms xs))
	end




