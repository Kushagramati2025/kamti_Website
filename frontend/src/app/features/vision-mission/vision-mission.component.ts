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
    vision: any;
    mission: any;
    loading = true;

    ngOnInit(): void {
        this.apiService.getVisionMission().subscribe({
            next: (data) => {
                this.vision = data.find(item => item.type === 'Vision');
                this.mission = data.find(item => item.type === 'Mission');
                this.loading = false;
            },
            error: () => {
                this.loading = false;
            }
        });
    }
}
