import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
    selector: 'app-vision-mission',
    standalone: true,
    imports: [CommonModule, RouterLink, RouterLinkActive],
    templateUrl: './vision-mission.component.html',
    styleUrl: './vision-mission.component.css'
})
export class VisionMissionComponent { }
