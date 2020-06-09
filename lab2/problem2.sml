fun revCycleHelper(L, i) = if null L then [i]
	else hd(L) :: revCycleHelper(tl(L), i);


fun revCycle(L) = revCycleHelper(tl(L), hd(L));


fun revCyclesHelper(L, i) = if i = 0 then L
    else revCyclesHelper(tl(L) @ [hd(L)], i-1);

fun revCycles(L, i) = if null L then []
    else revCyclesHelper(L, i);

revCycle([1,2,3,4,5,6]);
revCycle([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]);
revCycle(["mukesh", "goud", "kondeti"]);

revCycles([1.0, 2.0, 3.0, 4.0], 2);
revCycles([1, 2, 3, 4, 5, 6], 4);
revCycles(["mukesh", "goud", "kondeti"], 2);