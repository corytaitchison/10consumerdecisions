# SCDL1991 Sem 2 - 10. Supporting Consumer Decision Using Online Reviews

## FILES:

### Data Code:
Contains code that formatted and loaded the data
- `JSON_to_CSV_convert_Restaurants.ipynb`: Converts the JSON raw data into a CSV containing only restaurant reviews
- `loadRandom.py`: Loads in the CSV file with a required sample size and seed

### Stars:
Code for analysing stars and usefulness

### Linguistic:
- `LIWC_Adjectives_Adverbs.ipynb`: Analysis of adjectives and adverbs using the LIWC-analysed data
- `readability.py`: Analysis of readability scores, using the `readability_score` package

### readability_score:
Package to calculate the readability score. Cloned from https://github.com/wimmuskee/readability-score.

### Time:
Analysis of time features of the data.
- `Yearly_Weekday_Weekend.ipynb`: Yearly, Weekday and Weekend analysis
- `Hourly.ipynb`: Hourly analysis, combined with LIWC features
