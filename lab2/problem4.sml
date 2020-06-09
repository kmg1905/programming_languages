fun first(L) = 
	if L = nil then nil
	else hd(L)::fourth(tl(L))
and

fourth(L) 
	= if L=nil then nil
	else third(tl(L))

and

third(L) 
	= if L = nil then nil
	else second(tl(L))
and

second(L) 
	= if L=nil then nil
	else first(tl(L));


first([1,2,3,4,5,6,7,8,9,10,11,12,13]);
second([1,2,3,4,5,6,7,8,9,10,11,12,13]);
third([1,2,3,4,5,6,7,8,9,10,11,12,13]);
fourth([1,2,3,4,5,6,7,8,9,10,11,12,13]);

first([1,2,3,4,5,6,7,8,9,10,11,12,13, 14, 15, 16]);
second([1,2,3,4,5,6,7,8,9,10,11,12,13, 14, 15, 16]);
third([1,2,3,4,5,6,7,8,9,10,11,12,13, 14, 15, 16]);
fourth([1,2,3,4,5,6,7,8,9,10,11,12,13, 14, 15, 16]);