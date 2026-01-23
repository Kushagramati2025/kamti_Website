import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-vision-mission',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterLinkActive],
  templateUrl: './vision-mission.component.html',
  styleUrl: './vision-mission.component.css'
})
export class VisionMissionComponent implements OnInit {
  apiService = inject(ApiService);
  items: any[] = [];
  loading = true;

  ngOnInit() {
    this.apiService.getVisionMission().subscribe({
      next: (data) => {
        this.items = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('Error loading vision-mission:', err);
        this.loading = false;
      }
    });
  }
}
