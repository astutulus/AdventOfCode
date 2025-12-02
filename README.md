# Day 2

Had great fun optimising for part 1.

But seeing part 2 -- and remembering yesterday's experience in how forgiving the data volume -- decided to just smash through every number... 

```
Running: day_2.part_1
Time: 0.0004 seconds

Running: day_2.part_2_brute_force
Time: 2.0930 seconds
```

...as reflected in the timings!

# Day 1

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
