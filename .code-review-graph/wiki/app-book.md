# app-book

## Overview

Directory-based community: backend/app

- **Size**: 5 nodes
- **Cohesion**: 0.0000
- **Dominant Language**: python

## Members

| Name | Kind | File | Lines |
|------|------|------|-------|
| get_db | Function | D:\FE_BE_Code_Generator\Book-Tracker\backend\app\database.py | 16-21 |
| Book | Class | D:\FE_BE_Code_Generator\Book-Tracker\backend\app\models.py | 6-22 |
| BookCreate | Class | D:\FE_BE_Code_Generator\Book-Tracker\backend\app\schemas.py | 6-14 |
| BookUpdate | Class | D:\FE_BE_Code_Generator\Book-Tracker\backend\app\schemas.py | 17-25 |
| BookOut | Class | D:\FE_BE_Code_Generator\Book-Tracker\backend\app\schemas.py | 28-44 |

## Execution Flows

No execution flows pass through this community.

## Dependencies

### Outgoing

- `BaseModel` (3 edge(s))
- `SessionLocal` (1 edge(s))
- `close` (1 edge(s))
- `Base` (1 edge(s))

### Incoming

- `D:\FE_BE_Code_Generator\Book-Tracker\backend\app\schemas.py` (3 edge(s))
- `D:\FE_BE_Code_Generator\Book-Tracker\backend\app\database.py` (1 edge(s))
- `D:\FE_BE_Code_Generator\Book-Tracker\backend\app\models.py` (1 edge(s))
