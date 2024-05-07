% If choooseDay exists, then select a weekend day
numDays(1).
1 { select(DAY) : day(DAY) } NUM :- numDays(NUM).
