import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BookOut } from '../../../models/book.model';

@Component({
  selector: 'app-book-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './book-card.component.html',
  styleUrls: ['./book-card.component.css']
})
export class BookCardComponent {
  @Input() book!: BookOut;
  @Output() onDelete = new EventEmitter<number>();
  @Output() onSelect = new EventEmitter<number>();

  handleCardClick(): void {
    this.onSelect.emit(this.book.id);
  }

  handleDeleteClick(event: Event): void {
    event.stopPropagation();
    this.onDelete.emit(this.book.id);
  }

  getStatusBadgeClass(): string {
    switch (this.book.status.toLowerCase()) {
      case 'wishlist':
        return 'status-wishlist';
      case 'reading':
        return 'status-reading';
      case 'finished':
        return 'status-finished';
      default:
        return 'status-wishlist';
    }
  }

  getStatusLabel(): string {
    return this.book.status.charAt(0).toUpperCase() + this.book.status.slice(1);
  }

  getRatingArray(): number[] {
    return this.book.rating ? Array(this.book.rating).fill(0) : [];
  }
}