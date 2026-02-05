import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-leadership',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterLinkActive],
  templateUrl: './leadership.component.html',
  styleUrl: './leadership.component.css'
})
export class LeadershipComponent implements OnInit {
  apiService = inject(ApiService);
  leaders: any[] = [];
  loading = true;

  ngOnInit() {
    this.apiService.getLeadership().subscribe({
      next: (data) => {
        this.leaders = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('Error loading leadership:', err);
        this.loading = false;
      }
    });
  }

  getImageUrl(path: string | null): string {
    return this.apiService.getImageUrl(path || '');
  }
}
