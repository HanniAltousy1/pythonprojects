def main():
  quiz = [
    {
      "question": "What is the capital of France?",
      "choices": ["Paris", "London", "Rome"],
      "correct": "Paris"
    },
    {
      "question": "What is the largest planet in our solar system?",
      "choices": ["Earth", "Mars", "Jupiter"],
      "correct": "Jupiter"
    },
    {
      "question": "What is the chemical symbol for the element oxygen?",
      "choices": ["O", "O2", "O3"],
      "correct": "O2"
    }
  ]

  correct_answers = 0

  for question in quiz:
    print(question["question"])

    for i, choice in enumerate(question["choices"]):
      print(f"{i + 1}: {choice}")

    user_answer = input("Enter the correct answer: ")

    if user_answer == question["correct"]:
      print("Correct!")
      correct_answers += 1
    else:
      print("Incorrect!")

  print(f"You got {correct_answers} out of {len(quiz)} questions correct.")

main()