def greet_learner(name: str) -> str:
    return f"Welcome to AI Solutions Developer, {name}!"


learners = ["Alex", "Taylor", "Jordan"]

for learner in learners:
    print(greet_learner(learner))
