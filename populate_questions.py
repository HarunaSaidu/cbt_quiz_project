from quiz.models import Question

questions_data = [
    {
        'question_text': 'What is the main function of the CPU in a computer?',
        'option_a': 'To display images on the screen',
        'option_b': 'To process data and instructions',
        'option_c': 'To store files permanently',
        'option_d': 'To connect to the internet',
        'correct_answer': 'B',
        'explanation': 'CPU stands for Central Processing Unit and it processes all data and instructions.'
    },
    {
        'question_text': 'Which device is used to move the cursor on the screen?',
        'option_a': 'Keyboard',
        'option_b': 'Monitor',
        'option_c': 'Mouse',
        'option_d': 'Printer',
        'correct_answer': 'C',
        'explanation': 'The mouse is a pointing device used to move the cursor and select items on screen.'
    },
    {
        'question_text': 'What is the proper way to shut down a computer?',
        'option_a': 'Switch off the power directly',
        'option_b': 'Remove the power cable',
        'option_c': 'Use the Start menu and select Shut Down',
        'option_d': 'Press the reset button',
        'correct_answer': 'C',
        'explanation': 'Always use the proper shutdown procedure through the Start menu to avoid data loss.'
    },
    {
        'question_text': 'Which key is used to delete text before the cursor?',
        'option_a': 'Delete',
        'option_b': 'Backspace',
        'option_c': 'Enter',
        'option_d': 'Tab',
        'correct_answer': 'B',
        'explanation': 'Backspace deletes characters before (to the left of) the cursor.'
    },
    {
        'question_text': 'What does WWW stand for?',
        'option_a': 'World Wide Web',
        'option_b': 'World Wide Weather',
        'option_c': 'World Wide Work',
        'option_d': 'World Wide Wireless',
        'correct_answer': 'A',
        'explanation': 'WWW stands for World Wide Web, the system of interconnected web pages.'
    },
    {
        'question_text': 'Which part of the computer displays information?',
        'option_a': 'Keyboard',
        'option_b': 'Mouse',
        'option_c': 'Monitor',
        'option_d': 'CPU',
        'correct_answer': 'C',
        'explanation': 'The monitor (screen) displays all visual information from the computer.'
    },
    {
        'question_text': 'What is the function of the Enter key?',
        'option_a': 'Delete text',
        'option_b': 'Move to next line or confirm action',
        'option_c': 'Close programs',
        'option_d': 'Create spaces between words',
        'correct_answer': 'B',
        'explanation': 'Enter key moves to the next line in typing and confirms actions/commands.'
    },
    {
        'question_text': 'Which of these is an input device?',
        'option_a': 'Monitor',
        'option_b': 'Printer',
        'option_c': 'Speaker',
        'option_d': 'Keyboard',
        'correct_answer': 'D',
        'explanation': 'Input devices send information to the computer. Keyboard is an input device.'
    },
    {
        'question_text': 'What does CBT stand for in WAEC examinations?',
        'option_a': 'Computer Basic Test',
        'option_b': 'Computer Based Test',
        'option_c': 'Central Board Test',
        'option_d': 'Complete Book Test',
        'correct_answer': 'B',
        'explanation': 'CBT stands for Computer Based Test, where exams are taken on computers.'
    },
    {
        'question_text': 'Which button do you click to select an answer in a CBT exam?',
        'option_a': 'Right mouse button',
        'option_b': 'Left mouse button',
        'option_c': 'Scroll wheel',
        'option_d': 'Both buttons together',
        'correct_answer': 'B',
        'explanation': 'The left mouse button is used for selecting and clicking items.'
    },
    {
        'question_text': 'What is a folder in a computer used for?',
        'option_a': 'To print documents',
        'option_b': 'To organize and store files',
        'option_c': 'To connect to internet',
        'option_d': 'To play music',
        'correct_answer': 'B',
        'explanation': 'Folders help organize files, like drawers in a filing cabinet.'
    },
    {
        'question_text': 'Which key combination is used to copy text?',
        'option_a': 'Ctrl + V',
        'option_b': 'Ctrl + X',
        'option_c': 'Ctrl + C',
        'option_d': 'Ctrl + Z',
        'correct_answer': 'C',
        'explanation': 'Ctrl + C is the keyboard shortcut to copy selected text or items.'
    },
    {
        'question_text': 'What is the function of a web browser?',
        'option_a': 'To type documents',
        'option_b': 'To access and view websites',
        'option_c': 'To store files',
        'option_d': 'To edit photos',
        'correct_answer': 'B',
        'explanation': 'A web browser (like Chrome, Firefox, Edge) is used to access and view websites on the internet.'
    },
    {
        'question_text': 'Which of these is an output device?',
        'option_a': 'Mouse',
        'option_b': 'Scanner',
        'option_c': 'Keyboard',
        'option_d': 'Printer',
        'correct_answer': 'D',
        'explanation': 'Output devices receive information from the computer. A printer outputs printed documents.'
    },
    {
        'question_text': 'What does double-clicking the mouse do?',
        'option_a': 'Deletes items',
        'option_b': 'Opens files or programs',
        'option_c': 'Closes windows',
        'option_d': 'Saves documents',
        'correct_answer': 'B',
        'explanation': 'Double-clicking (clicking left button twice quickly) opens files and programs.'
    },
    {
        'question_text': 'Which key makes all letters CAPITAL when pressed once?',
        'option_a': 'Shift',
        'option_b': 'Tab',
        'option_c': 'Caps Lock',
        'option_d': 'Enter',
        'correct_answer': 'C',
        'explanation': 'Caps Lock toggles capital letters on and off. Press once to enable, again to disable.'
    },
    {
        'question_text': 'What is the Desktop in a computer?',
        'option_a': 'The physical table where computer sits',
        'option_b': 'The main screen showing icons and taskbar',
        'option_c': 'The keyboard area',
        'option_d': 'The mouse pad',
        'correct_answer': 'B',
        'explanation': 'The Desktop is the main screen you see when computer starts, showing icons, taskbar, and wallpaper.'
    },
    {
        'question_text': 'Where is the Start button usually located in Windows?',
        'option_a': 'Top right corner',
        'option_b': 'Top left corner',
        'option_c': 'Bottom right corner',
        'option_d': 'Bottom left corner',
        'correct_answer': 'D',
        'explanation': 'The Start button is typically located at the bottom left corner of the screen in the taskbar.'
    },
    {
        'question_text': 'What is the purpose of the Recycle Bin?',
        'option_a': 'To store important files',
        'option_b': 'To temporarily store deleted files',
        'option_c': 'To run programs',
        'option_d': 'To connect to internet',
        'correct_answer': 'B',
        'explanation': 'The Recycle Bin temporarily stores deleted files, allowing you to recover them if needed.'
    },
    {
        'question_text': 'Which mouse action is used to see more options?',
        'option_a': 'Left click',
        'option_b': 'Double click',
        'option_c': 'Right click',
        'option_d': 'Scroll wheel',
        'correct_answer': 'C',
        'explanation': 'Right-clicking opens a context menu with additional options for the selected item.'
    },
    {
        'question_text': 'What does URL stand for?',
        'option_a': 'Universal Resource Locator',
        'option_b': 'Uniform Resource Locator',
        'option_c': 'United Resource Link',
        'option_d': 'Universal Reference Link',
        'correct_answer': 'B',
        'explanation': 'URL stands for Uniform Resource Locator - the address of a website (like www.google.com).'
    },
    {
        'question_text': 'Which key moves the cursor to the next field without using the mouse?',
        'option_a': 'Enter',
        'option_b': 'Space',
        'option_c': 'Tab',
        'option_d': 'Shift',
        'correct_answer': 'C',
        'explanation': 'The Tab key moves the cursor to the next field or section, useful for filling forms.'
    },
    {
        'question_text': 'In a CBT exam, what should you do if you want to review a question later?',
        'option_a': 'Close the browser',
        'option_b': 'Skip it and use the previous button to return',
        'option_c': 'Refresh the page',
        'option_d': 'Open a new tab',
        'correct_answer': 'B',
        'explanation': 'You can skip questions and use navigation buttons to return and review them later.'
    },
    {
        'question_text': 'What is the Space Bar used for?',
        'option_a': 'To delete text',
        'option_b': 'To create space between words',
        'option_c': 'To save documents',
        'option_d': 'To close windows',
        'correct_answer': 'B',
        'explanation': 'The Space Bar creates spaces between words when typing.'
    },
    {
        'question_text': 'What should you do before shutting down a computer?',
        'option_a': 'Remove the keyboard',
        'option_b': 'Close all programs and save your work',
        'option_c': 'Disconnect the monitor',
        'option_d': 'Delete all files',
        'correct_answer': 'B',
        'explanation': 'Always close programs and save work before shutting down to prevent data loss.'
    },
]

# Create questions
for q_data in questions_data:
    Question.objects.create(**q_data)

print(f"Successfully created {len(questions_data)} questions!")