# DecisionWheel
Graphical decision wheel, to decide where to go to lunch

To use: Edit the "decisionlist" in pythonball.pyw to include the desired choices. Run program. Click anywhere in window to spin again if unsatisfied.

# Dependencies:
'Choice 1' has a 50% chance of being selected.
'Choice 2' has a 25% chance.
'Choice 3' has a 20% chance.
'Choice 4' has a 5% chance.

 -The weighted_random_choice function uses the random.choices() method to select an item from decisionlist based on the probabilities list. 
 -random.choices(choices, weights) returns a list of choices selected based on their weights. Since you want only one choice, [0] extracts the single item from the list.

-cd to DecisionWheel
then type in terminal :
-python ChoiceWheel.pyw
