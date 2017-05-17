# Compute Acquisition Quality of Fortune 500 companies

## Phase 1: M&A data mining  
This phase currently involves using files containing html tables manually copied from wikipedia pages such as [this one](https://en.wikipedia.org/wiki/List_of_mergers_and_acquisitions_by_Apple)

to turn this into a more readable file run (under the current implementation):  
`python m_and_a_crawl\table_converter -f m_and_a_crawl\tables\wiki_apple_acq.html -t Date Company -o out.txt -k AAPL`  
from the F500 directory
or  
`python m_and_a_crawl\table_converter -h` for help

## Phase 2: Stock historical values  
This phase is currently under construction under the `m_and_a_quality` module

## Phase 3: Quality quantification stage  
While this stage is not yet implemented, the heurisitc used to measure quality of an aquisition is based on the market's
reaction to the acquisition announcement:

Let us define:
* **Pre7**: the average value of the stock during the 7 days prior to the acquisition
* **Pre30**: the average value of the stock during the 30 days prior to the acquisition
* **Pre23**: the average value of the stock during the 23 days prior to 7 days before the acquisition (intuitively, Pre30 without Pre7)
* **Post7**: the average value of the stock during the 7 days after the acquisition

* **PreTrend**: (Pre7-Pre23)/Pre30
* **PostTrend**: (Post7-Pre30)/Pre30

* **Quality**: (PostTrend-PreTrend)/PreTrend

## Phase 4: Visualization  
This phase is not yet under construction.

