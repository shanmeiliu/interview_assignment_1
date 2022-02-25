# Assumptions
- All input sources have the same formatting at the output sources
  - Naturally I would change formats if the source didn't match. I did not show an example of this.
- Provided sample is representative of the inputs
- That the output simply print to the screen. I see no indication that this would be a (micro)service that is called to provide json. 
- That this shouldn't consume considerable time to solve. (Simple request => simple response.)
 
# Process
- First I took the sample output json data and manually created two 
  source files from it
  - team_rankings.json (Changed the labels, Deduplicated the rows)
  - scoreboard.json (Changed the labels)
  - Added 1 addtional entry to each to simulate diffrent data

- Created a trivial flask application to serve these two files from 
  simulated endpoints. This is a VERY minimal example that provides endpoints I can connect to. It completely ignores the parameters, but is sufficient to test etl example

- Created a python application that would query the endpoints and merge 
  the data, exporting the desired json

# How to run
- Inside a python environment (3.92) that has flask (1.1.2) installed.(Instructions not provided)
- There are two processes (one to simulate the endpoints, one to show the etl example)
- Run: `FLASK_APP=simulated-host.py flask run`
- Run: `python etl.py`

# Thoughts
- Naturally there are many edge cases not considered in this code. (These edge cases would accounted for and managed in production code)
  - Endpoint doesn't respond or some form of error code
  - Endpoint doesn't provide valid json  
  - Endpoint doesn't provide data
  - Json doesn't contain the correct fields
  - Json contains more fields
  - Json labels are not the correct case
  - Team_rankings is missing a team that exists in scoreboard
  - Source/Output formatting differences (as above)
- In production I would create unit tests for regression testing
- In production I would turn this into a proper (micro)service
