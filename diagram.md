```mermaid 
flowchart TD
A[Start]--> B[Display Menu]
B --> C{Choose option}

C --> D[Add student]
C --> E[View student]
C --> F[Delete student]
C --> G[update student]
C --> H[Search student] 
C --> I[Add marks]
C --> J[View result]
C --> K[Exit]

D --> B
E --> B
F --> B
G --> B
H --> B
I --> B
J --> B
K --> L[End]
```