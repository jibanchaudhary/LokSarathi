Loksarathi is an educational application offering reference books, quizzes, PDFs, and notices related to Lok Sewa. It serves as a comprehensive resource platform to help users prepare for educational and competitive exams.

<img width="1470" alt="Screenshot 2024-09-30 at 11 30 36 AM" src="https://github.com/user-attachments/assets/6087ed44-af9b-4ea9-a6f8-b166b83373b6">

The Loksarathi pre-login interface is designed with a clean and responsive layout using HTML5, CSS3, and Django templating. The focus is on providing an intuitive entry point for users, with minimal distractions and quick access to essential features.

Technical Features:

Search Functionality: Implemented with an input field that enables users to search for notes stored in the MySQL database. Search queries are processed via Django views and filtered with Django ORM.

Modular Components: The interface utilizes a modular card-based layout for organizing sections like Study Materials, Practice Tests, and Notices. These sections are dynamically populated through back-end models.

User Authentication: The navigation bar provides options for Sign In and Register, leveraging Django's built-in authentication system.

<img width="1469" alt="Screenshot 2024-09-30 at 11 36 56 AM" src="https://github.com/user-attachments/assets/904a5a75-8fcd-4c5d-96dc-21450cceba38">

Once authenticated, the post-login interface expands to offer additional features such as access to the Syllabus, Study Materials, Previous Year Questions, Games, and Notices. It follows responsive design for a smooth experience across devices.



