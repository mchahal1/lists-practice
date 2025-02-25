# TASK: Create a high score tracker that keeps the top 5 scores.
# Define a function that takes a list of scores and a new score
def updatescores(scores: list, new_score: int) -> list:
    """Updates the list of top 5 high scores by adding a new score and keeping only the highest."""
    scores.append(new_score)  # Append the new score to the list
    scores.sort(reverse=True) # Sort the list in descending order
    # Return the updated list
    return scores[:5] # Keep only the top 5 scores

# Start with an empty high scores list
high_scores = []

# Use a loop to let the user enter scores until they type -1
while True:
    new_score = int(input("Enter a new score (or -1 to stop): "))
    if new_score == -1:
        break
    high_scores = updatescores(high_scores, new_score)
    # Call the function with each new score and display the updated top 5 scores
    print(f"Updated high scores: {high_scores}")










