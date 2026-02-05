import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ApiService } from '../../core/services/api.service';
import { inject } from '@angular/core';

@Component({
    selector: 'app-leaders-innovating',
    standalone: true,
    imports: [CommonModule],
    templateUrl: './leaders-innovating.component.html',
    styleUrl: './leaders-innovating.component.css'
})
export class LeadersInnovatingComponent {
    apiService = inject(ApiService);
}
