fun remove(x,L) = if null L then []
	else if x = hd(L) then tl(L)
	else hd(L)::remove(x,tl(L));

fun reverse(L) =
	if null L then nil
	else reverse(tl(L)) @ [hd(L)];

fun remove2(x,L) = if null L then []
	else if x = hd(L) then tl(L)
	else hd(L)::remove2(x,tl(L));


fun removeLst(x,L) = reverse(remove2(x, reverse(L)));



remove(3, [1,3,5,2,3,4]);
remove("nani", ["mukesh", "nani", "mukesh", "nani", "nani"]);

remove(false, [false,true,false,false]);

removeLst(3, [1,3,5,2,3,4]);
removeLst("nani", ["mukesh", "nani", "mukesh", "nani", "nani"]);
removeLst(false, [false,true,false,false]);
