# GuessThePlayer ⚽❓
Implementation of a POC for a football game where the player has to guess the hidden football player by his similarity with others.

Players' data are taken from the website FBref: https://fbref.com/it/   
Inspired by: https://playfootball.games/contextinho/

# Description 📓
Starting from players' data, a graph db using Neo4j was created.   
Node labels included:  
- Nation  
- Player  
- Team (one label per season)  
- Position  

Relationship types included:  
- PLAYED_FOR  
- IS_NATION  
- POSITION_PLAYED  

After that, it was run the NodeSimilarity algorithm from the GDS library to compute similarity scores.   
At the end, results were stored and UI POC was created.
