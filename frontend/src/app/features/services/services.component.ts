import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { ApiService } from '../../core/services/api.service';
import { BannerCarouselComponent } from '../../shared/components/banner-carousel/banner-carousel.component';

@Component({
  selector: 'app-services',
  standalone: true,
  imports: [CommonModule, RouterLink, BannerCarouselComponent],
  templateUrl: './services.component.html',
  styleUrl: './services.component.css'
})
export class ServicesComponent implements OnInit {
  apiService = inject(ApiService);
  activeTab: string = 'Kusha at glance';

  tabs = [
    'Kusha at glance',
    'Application Services',
    'Data Analytics',
    'Embedded-Software'
  ];

  ngOnInit() {
    // Initial data loading if needed
  }

  setActiveTab(tab: string) {
    this.activeTab = tab;
  }
}
