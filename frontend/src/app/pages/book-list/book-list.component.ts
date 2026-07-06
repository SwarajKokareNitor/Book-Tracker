import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { debounceTime, Subject } from 'rxjs';
import { BookService } from '../../core/services/book.service';
import { BookOut } from '../../models/book.model';
import { BookCardComponent } from '../../shared/components/book-card/book-card.component';

@Component({
  selector: 'app-book-list',
  standalone: true,
  imports: [CommonModule, FormsModule, BookCardComponent],
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css']
})
export class BookListComponent implements OnInit {
  books: BookOut[] = [];
  allBooks: BookOut[] = [];
  selectedStatus: string = 'all';
  selectedGenre: string = 'all';
  searchText: string = '';
  genres: string[] = [];

  private searchSubject = new Subject<string>();

  constructor(
    private bookService: BookService,
    private router: Router
  ) {
    this.searchSubject.pipe(
      debounceTime(300)
    ).subscribe(searchValue => {
      this.searchText = searchValue;
      this.loadBooks();
    });
  }

  ngOnInit(): void {
    this.loadBooks();
  }

  loadBooks(): void {
    const filters: { status?: string; genre?: string; search?: string } = {};

    if (this.selectedStatus !== 'all') {
      filters.status = this.selectedStatus;
    }

    if (this.selectedGenre !== 'all') {
      filters.genre = this.selectedGenre;
    }

    if (this.searchText) {
      filters.search = this.searchText;
    }

    this.bookService.getBooks(filters).subscribe(books => {
      this.books = books;
      this.allBooks = books;
      this.extractGenres();
    });
  }

  extractGenres(): void {
    const genreSet = new Set<string>();
    this.allBooks.forEach(book => {
      if (book.genre) {
        genreSet.add(book.genre);
      }
    });
    this.genres = Array.from(genreSet).sort();
  }

  onStatusChange(status: string): void {
    this.selectedStatus = status;
    this.loadBooks();
  }

  onGenreChange(event: Event): void {
    const target = event.target as HTMLSelectElement;
    this.selectedGenre = target.value;
    this.loadBooks();
  }

  onSearchChange(event: Event): void {
    const target = event.target as HTMLInputElement;
    this.searchSubject.next(target.value);
  }

  onBookDelete(id: number): void {
    if (confirm('Are you sure you want to delete this book?')) {
      this.bookService.deleteBook(id).subscribe(() => {
        this.books = this.books.filter(book => book.id !== id);
        this.allBooks = this.allBooks.filter(book => book.id !== id);
        this.extractGenres();
      });
    }
  }

  onBookSelect(id: number): void {
    this.router.navigate(['/books', id]);
  }

  navigateToNewBook(): void {
    this.router.navigate(['/books/new']);
  }
}