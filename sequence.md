``` mermaid
sequenceDiagram
actor user
participant SMS as student management system
participant Data as student data

User->>SMS: Select Add student
SMS->>User: Ask Student ID and Name
User->>SMS: Enter student details
SMS->>data: store student 
Data->>SMS: Student saved
SMS-->>User:student added successfully
User->>SMS: Select Add marks
SMS->>User: Ask Student ID and marks
User->>SMS: Enter marks
SMS->>data: update student marks
Data->>SMS: marks updated
SMS-->>User:marks added successfully
User->>SMS: select view result
SMS->>data: get student marks
Data->>SMS: return marks
SMS-->>User:Display result
```