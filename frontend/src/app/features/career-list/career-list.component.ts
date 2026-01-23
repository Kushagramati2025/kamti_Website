import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { ApiService } from '../../core/services/api.service';
import { BannerCarouselComponent } from '../../shared/components/banner-carousel/banner-carousel.component';

@Component({
  selector: 'app-career-list',
  standalone: true,
  imports: [CommonModule, RouterLink, BannerCarouselComponent],
  templateUrl: './career-list.component.html',
  styleUrl: './career-list.component.css'
})
export class CareerListComponent implements OnInit {
  apiService = inject(ApiService);
  jobs: any[] = [];
  loading = true;

  ngOnInit() {
    this.apiService.getCareers().subscribe(data => {
      this.jobs = data;
      this.loading = false;
    });
  }
}
