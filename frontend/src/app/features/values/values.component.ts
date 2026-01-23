import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-values',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterLinkActive],
  templateUrl: './values.component.html',
  styleUrl: './values.component.css'
})
export class ValuesComponent implements OnInit {
  apiService = inject(ApiService);
  values: any[] = [];
  loading = true;

  ngOnInit() {
    this.apiService.getValues().subscribe({
      next: (data) => {
        this.values = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('Error loading values:', err);
        this.loading = false;
      }
    });
  }
}
