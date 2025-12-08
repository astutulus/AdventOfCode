## Day 8

Definitely the most involved yet.

Got the day off to a great start, that I managed to finish part 1 by `08:35 am`

Very happy I used **classes** to keep organised today. Really saved on dev time.

Part 2 needed lots more thought, but just a few more fields and methods.

## Day 7

Beautiful and relaxing; most enjoyable yet!

## Day 6

Part 2 was my most longwinded yet, in an effort to keep it clear to myself.

Added debug `print()` and even some `try` blocks, in case data had been "ragged" (so final sums incomplete).

Turned out the input text had been prepared extra-friendly, with extra spaces to avoid this issue.

## Day 5

### Part 1 

Just a question of how much fun you want to have tidying the code!

Mostly left it verbose but was happy to brush up on the Python `map()` function.

### Part 2

Relaxing. Learnt about Python `enumerate` to walk through list from second element.

## Day 4

Went for one giant list, but a 2D array would've made it simpler to keep in range, at west and east edges of each row.   

## Day 3

Didn't bother timing as negligible volume of input data, given I think the task runs in O(n) time.

Indeed appears instant — despite adding up to over a million billion! What a world we live in.

## Day 2

Had great fun optimising for part 1.

But seeing part 2 -- and remembering yesterday's experience in how forgiving the data volume -- decided to just smash through every number... 

```
Running: day_2.part_1
Time: 0.0004 seconds

Running: day_2.part_2_brute_force
Time: 2.0930 seconds
```

...as reflected in the timings!

## Day 1

After producing the performant solution I was brushing my teeth, when I wondered whether a simple, "one click at a time" solution would have been prohibatively slow.

I am accustiomed to challenges where brute force is simply impossible i.e. times out, so I was really surprised it finished instantly.

This made me want to add a timer. Here is some sample output (timings vary on each run):

```
Running: part_1
Time: 0.0010 seconds

Running: part_2_a
Time: 0.0010 seconds

Running: part_2_b_brute_force
Time: 0.0214 seconds
```

I think I wrote the brute force algorithm in under 1% the time of the original solution - which itself could be an advantage in some situations.

However the input data for this challenege was very lenient. With serious numbers, the brute force approach would become untenable.
