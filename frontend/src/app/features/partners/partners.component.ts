import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-partners',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterLinkActive],
  templateUrl: './partners.component.html',
  styleUrl: './partners.component.css'
})
export class PartnersComponent implements OnInit {
  apiService = inject(ApiService);
  partners: any[] = [];
  loading = true;

  ngOnInit() {
    this.apiService.getPartners().subscribe({
      next: (data) => {
        this.partners = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('Error loading partners:', err);
        this.loading = false;
      }
    });
  }
}
