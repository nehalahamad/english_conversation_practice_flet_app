import flet as ft

def main(page: ft.Page):
    page.title = "MCQ App with Wrapped Options"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Define the MCQ data
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris",
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars",
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
            "answer": "Harper Lee",
        },
        {
            "question": "What is the longest river in the world?",
            "options": [
                "The Nile, which flows through northeastern Africa",
                "The Amazon, which flows through South America",
                "The Yangtze, which flows through China",
                "The Mississippi, which flows through the United States",
            ],
            "answer": "The Nile, which flows through northeastern Africa",
        },
    ]

    # Track the current question index
    current_question_index = 0

    # Radio group for options
    radio_group = ft.RadioGroup(content=ft.Column())

    # Feedback text
    feedback_text = ft.Text(size=16, weight="bold")

    def load_question():
        """Load the current question and options."""
        question_data = questions[current_question_index]
        radio_group.content.controls = [
            ft.Row(
                [
                    ft.Radio(value=option),  # Radio button
                    ft.Text(option, width=page.width - 100, wrap=True),  # Wrapped text
                ],
                spacing=10,
            )
            for option in question_data["options"]
        ]
        question_text.value = f"Q{current_question_index + 1}: {question_data['question']}"
        feedback_text.value = ""
        page.update()

    def submit_answer(e):
        """Check the selected answer and display feedback."""
        selected_answer = radio_group.value
        correct_answer = questions[current_question_index]["answer"]

        if selected_answer == correct_answer:
            feedback_text.value = "Correct! 🎉"
            feedback_text.color = ft.colors.GREEN
        else:
            feedback_text.value = f"Incorrect! The correct answer is {correct_answer}."
            feedback_text.color = ft.colors.RED

        page.update()

    def next_question(e):
        """Move to the next question."""
        global current_question_index
        if current_question_index < len(questions) - 1:
            current_question_index += 1
            load_question()
        else:
            feedback_text.value = "You have completed all questions!"
            feedback_text.color = ft.colors.BLUE
            page.update()

    # Question text
    question_text = ft.Text(size=20, weight="bold")

    # Submit button
    submit_button = ft.ElevatedButton(text="Submit", on_click=submit_answer)

    # Next button
    next_button = ft.ElevatedButton(text="Next", on_click=next_question)

    # Load the first question
    load_question()

    # Add all controls to the page
    page.add(
        question_text,
        radio_group,
        ft.Row([submit_button, next_button], alignment=ft.MainAxisAlignment.CENTER),
        feedback_text,
    )

ft.app(target=main)