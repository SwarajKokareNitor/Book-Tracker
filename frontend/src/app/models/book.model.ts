export interface BookCreate {
  title: string;
  author: string;
  genre?: string;
  status?: string;
  rating?: number;
  total_pages?: number;
  notes?: string;
  cover_color?: string;
}

export interface BookUpdate {
  title?: string;
  author?: string;
  genre?: string;
  status?: string;
  rating?: number;
  total_pages?: number;
  notes?: string;
  cover_color?: string;
}

export interface BookOut {
  id: number;
  title: string;
  author: string;
  genre?: string;
  status: string;
  rating?: number;
  total_pages?: number;
  notes?: string;
  cover_color?: string;
  created_at: string;
  updated_at: string;
}