# book-list-book

## Overview

Directory-based community: frontend/src/app/pages/book-list

- **Size**: 14 nodes
- **Cohesion**: 0.5385
- **Dominant Language**: typescript

## Members

| Name | Kind | File | Lines |
|------|------|------|-------|
| BookListComponent | Class | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 17-108 |
| constructor | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 27-37 |
| searchValue | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 33-36 |
| ngOnInit | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 39-41 |
| loadBooks | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 43-63 |
| books | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 58-62 |
| extractGenres | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 65-73 |
| book | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 95-95 |
| onStatusChange | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 75-78 |
| onGenreChange | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 80-84 |
| onSearchChange | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 86-89 |
| onBookDelete | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 91-99 |
| onBookSelect | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 101-103 |
| navigateToNewBook | Function | D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts | 105-107 |

## Execution Flows

- **onBookDelete** (criticality: 0.36, depth: 1)
- **books** (criticality: 0.28, depth: 1)
- **searchValue** (criticality: 0.24, depth: 1)
- **ngOnInit** (criticality: 0.24, depth: 1)
- **onStatusChange** (criticality: 0.24, depth: 1)
- **onGenreChange** (criticality: 0.24, depth: 1)

## Dependencies

### Outgoing

- `subscribe` (3 edge(s))
- `navigate` (2 edge(s))
- `filter` (2 edge(s))
- `add` (1 edge(s))
- `pipe` (1 edge(s))
- `debounceTime` (1 edge(s))
- `forEach` (1 edge(s))
- `sort` (1 edge(s))
- `from` (1 edge(s))
- `getBooks` (1 edge(s))
- `confirm` (1 edge(s))
- `deleteBook` (1 edge(s))
- `next` (1 edge(s))

### Incoming

- `D:\FE_BE_Code_Generator\Book-Tracker\frontend\src\app\pages\book-list\book-list.component.ts` (1 edge(s))
