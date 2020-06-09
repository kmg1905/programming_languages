fun square(n:real) = n * n;
fun cube(n:real) = n * n * n;

fun mul(d:real, n:int) = if n = 0 then 0.0
	else if n = 1 then d
	else d * mul(d, n - 1);

fun tabulate1(a:real, d:real, n:int, f, x:int) = if x = n+1 then []
	else
	(a+mul(d,x), f(a+mul(d,x)))::tabulate1(a,d,n,f, x+1);
	
fun tabulate(a:real,d:real,n:int,f) = tabulate1(a:real,d:real,n:int,f, 0);

tabulate(0.1, 2.0,  2, square);
tabulate(0.1, 2.2,  2, square);
tabulate(0.1, 2.2,  2, cube);