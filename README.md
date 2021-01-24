# spider_mtg


### Goal 

This is my attempt at scrapping Legacy decklists from mtgtop8.com, and also understanding how to scrape online content in general. The overall goal of this project is to compile a large dataset of Legacy decklists for personal analysis. Legacy is a Magic the Gathering format. This readme and the different files of this folder will be edited as I make progress, so stay tuned for more updates!

### How it works

[mtgtop8](https://www.mtgtop8.com) uses sub-archetypes to classify decks: Goblins, Elves, UR Delver, 4C Control, etc. On the screenshot below, each one of the archetype corresponds to a link. Once we follow one of these links, we get access to a list of decks played at various events by different player. The goal here is to only access decklists. I am not interested in where, when and by whom it was played.  

![Screenshot of mtgtop8](capture_mtgtop8)

[The Scrapy tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html) is pretty good and started this project following it. When you set up a new project with Scrapy, the folders are generated automatically. What you then need to do is to create "spiders" and store them under <code> <i>spider_mtg/spiders</i> </code>. A spider is a class defining how to follow links, how to extract desired information and so on.

To get what I needed, I created 3 differents spiders:

|  Spider                                 | Action                                                                                                     |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------|
|<code> <i>archetype_links.py</i> </code> | Collect all archetype links and store them in a file: <code> <i>archetypes.txt</i> </code> .               | 
|<code> <i>deck_links.py</i> </code>      | For each archetype, collect all deck links and store them in a file: <code> <i>decklinks.txt</i> </code>.  |
|<code> <i>deck_lists.py</i> </code>      | For each deck link, collect the decklist and store it in a file: <code> <i>decks_raw/deck_XXX/</i> </code>.|

You need to run the spiders in that order : <code> <i>archetype_links.py</i> -> <i>deck_links.py</i> -> <i>deck_lists.py</i> </code>. Please note that in the second step, collecting the deck links, I also use [Selenium](https://www.selenium.dev/selenium/docs/api/py/api.html) to automate web browser interaction. When collecting the deck links, I was not able to follow links to other page. Maybe I did not look hard enough for the next page CSS selector, but I wanted to move on and it was quicker to use <code> <i>selenium</i>.

Finally, note that I was a bit lazy and did not format the raw deck files. They contains ugly bits of html not really readable at first glance. Therefore, I wrote <code> <i>format_decklist.py</i> </code> to format the raw deck files into readable txt files (￣ｰ￣)ﾉ.  

### Disclaimer 

The information presented here about Magic: The Gathering is copyrighted by Wizards of the Coast. This project is not produced, endorsed, supported, or affiliated with Wizards of the Coast. 

<https://www.mtgtop8.com/> is the source of my data. This project would not have been possible without their amazing work!

This project is licensed under the MIT License.
