This program will take a set of queries written in a JSON file and output a CSV file with all of the cards that match the queries in the sets.

Queries should be written like<br>
1. "Wilhelt_BoardWipe": "ci:BU o:/(destroy|exile) (all|each)/",
2. "Wilhelt_SpotRemoval": "ci:BU (o:'exile target' or o:'destroy target' or o:/opponent sacrifices/ or o:/\\smm/) -o:-0",
3. "Wilhelt_Counterspell": "ci:UB o:/counter target.*spell/"
<p> This will make a column named Wilhelt and in the cell for each card which matches the given condition a row will be created in the CSV with each condition that it meets.
