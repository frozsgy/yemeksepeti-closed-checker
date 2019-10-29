# yemeksepeti-closed-checker
Checks if a specific restaurant that just temporarily stopped taking orders due to excessive orders is back online on yemeksepeti

I was just ordering something on yemeksepeti, but when I clicked the "place order" button, I got a nasty warning saying that "this restaurant is temporarily unavailable due to excessive orders". I got super angry because after spending many hours on deciding what to get, I was being told that I cannot place my order! GIMME MY FOOD! Anyways, I decided instead of refreshing the page every second, I can write a simple python script to do it for me. And it did! It did wonders!

Run it on your favourite terminal with Python 3.

Works if the restaurant is not accepting orders due to congestion or a temporarily problem.

## Dependencies
<ul><li>Requests</li></ul>

## CLI Commands
Instead of pasting the URL all the time, you can use the url as a CLI command.

Example:
```
python ys.py http://yemeksepeti.com/my-beautiful-sushi-place
```
