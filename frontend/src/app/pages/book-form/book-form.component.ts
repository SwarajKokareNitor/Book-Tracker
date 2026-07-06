import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { BookService } from '../../core/services/book.service';
import { BookCreate } from '../../models/book.model';

@Component({
  selector: 'app-book-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './book-form.component.html',
  styleUrls: ['./book-form.component.css']
})
export class BookFormComponent implements OnInit {
  bookForm!: FormGroup;
  submitted = false;

  statusOptions = [
    { value: 'wishlist', label: 'Wishlist' },
    { value: 'reading', label: 'Reading' },
    { value: 'finished', label: 'Finished' }
  ];

  colorSwatches = [
    '#e74c3c',
    '#3498db',
    '#2ecc71',
    '#f39c12',
    '#9b59b6',
    '#1abc9c'
  ];

  constructor(
    private fb: FormBuilder,
    private bookService: BookService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.bookForm = this.fb.group({
      title: ['', Validators.required],
      author: ['', Validators.required],
      genre: [''],
      status: ['wishlist'],
      rating: ['', [Validators.min(1), Validators.max(5)]],
      total_pages: [''],
      notes: [''],
      cover_color: ['#3498db']
    });
  }

  get f() {
    return this.bookForm.controls;
  }

  selectColor(color: string): void {
    this.bookForm.patchValue({ cover_color: color });
  }

  onSubmit(): void {
    this.submitted = true;

    if (this.bookForm.invalid) {
      return;
    }

    const formValue = this.bookForm.value;
    const payload: BookCreate = {
      title: formValue.title,
      author: formValue.author,
      genre: formValue.genre || undefined,
      status: formValue.status,
      rating: formValue.rating ? Number(formValue.rating) : undefined,
      total_pages: formValue.total_pages ? Number(formValue.total_pages) : undefined,
      notes: formValue.notes || undefined,
      cover_color: formValue.cover_color
    };

    this.bookService.createBook(payload).subscribe(() => {
      this.router.navigate(['/books']);
    });
  }

  onCancel(): void {
    this.router.navigate(['/books']);
  }
}