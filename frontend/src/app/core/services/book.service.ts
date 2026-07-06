import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { BookCreate, BookUpdate, BookOut } from '../../models/book.model';

@Injectable({
  providedIn: 'root'
})
export class BookService {
  constructor(private http: HttpClient) {}

  getBooks(filters?: { status?: string; genre?: string; search?: string }): Observable<BookOut[]> {
    let params = new HttpParams();

    if (filters) {
      if (filters.status) {
        params = params.set('status', filters.status);
      }
      if (filters.genre) {
        params = params.set('genre', filters.genre);
      }
      if (filters.search) {
        params = params.set('search', filters.search);
      }
    }

    return this.http.get<BookOut[]>(`${environment.apiUrl}/books`, { params });
  }

  getBook(id: number): Observable<BookOut> {
    return this.http.get<BookOut>(`${environment.apiUrl}/books/${id}`);
  }

  createBook(payload: BookCreate): Observable<BookOut> {
    return this.http.post<BookOut>(`${environment.apiUrl}/books`, payload);
  }

  updateBook(id: number, payload: BookUpdate): Observable<BookOut> {
    return this.http.patch<BookOut>(`${environment.apiUrl}/books/${id}`, payload);
  }

  deleteBook(id: number): Observable<void> {
    return this.http.delete<void>(`${environment.apiUrl}/books/${id}`);
  }
}