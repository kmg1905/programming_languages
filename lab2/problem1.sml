fun genPoly(n) = if n < 0 then []
	else 1.0 :: genPoly(n-1);

fun pow(a:real, index) = if index < 0 then 0.0
	else if index = 0 then 1.0
	else a * pow(a, index - 1);

fun evalPolyHelper(P:real list, a:real, index) = if null P then 0.0
	else (hd(P) * pow(a, index)) + evalPolyHelper(tl(P), a, index + 1);

fun evalPoly(P, a) = evalPolyHelper(P, a, 0);

fun reverse(L) =
	if null L then nil
	else reverse(tl(L)) @ [hd(L)];

fun add(A:real list,B:real list) = if null A then B
    else if null B then A
    else hd(A) + hd(B) :: add(tl(A), tl(B));
    
fun mulEle(A:real, B:real list) = if null B then []
    else A*hd(B) :: mulEle(A, tl(B));
    
fun mul(A:real, B:real list, n) = if n = 0 then mulEle(A, B)
    else 0.0 :: mul(A,B, n-1);
    
fun product(A,B,n) = if null A then []
    else add(mul(hd(A), B, n), product(tl(A), B, n+1));
    
fun multPoly(A,B) = if null A then []
    else if null B then []
    else product(reverse(A),reverse(B),0);
    



genPoly(3);
genPoly(5);

evalPoly([10.0, 3.0, 1.0], 2.0);
evalPoly([10.0, 3.0, 2.0], 2.0);

reverse(multPoly([~1.0,1.0], [1.0,1.0]));
reverse(multPoly([~1.0,1.0, 1.0], [1.0,1.0, 1.0]));


