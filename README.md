# war-game
Implementation of the card game "War" for Intel's interview process.

## Developer Setup
This project uses python 3.9 and pipenv

Install requirements: ```pipenv install```

From the root project directory, to execute the game:
`python -m src.games.war`

To run the tests:
```pytest```



## If I Had More Time
If I had more time I would clean up the war.py file and break it into several discrete
functions. The functions in war.py especially I would have liked to have had more time
to complete in a different way.

I also wanted to write examples of the flexibility of my implementation.
I did start this by including other playing card suit types - German, Latin, etc. -
but did not have enough time to demonstrate the same flexibility with deck creation
and card game implementations.

I would have also written more tests.

The last thing I would have done would be to create a UI, as I originally intended, 
using TKinter to stay within the Python requirement of the assignment.


## Considerations
I wanted to have classes that were usable for other playing card games, so I designed 
my classes with reusability and flexibility in mind. I wanted the code to be testable,
so while I had the time to do so, I made my code as modular as possible, following the single
responsibility principle (again, while I had time).

Edge cases considered:

When a card game/deck has jokers present, the initialization of the deck and hands is 
different, and needs to not break in such a scenario.

When a player does not have enough cards to continue a war, the game needs to end
immediately instead of attempting and failing to execute a war.