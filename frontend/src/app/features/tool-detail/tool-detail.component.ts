import { Component, inject, signal, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterModule, Router } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-tool-detail',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './tool-detail.component.html',
  styleUrl: './tool-detail.component.css' // Note: using default css file for now, might be empty
})
export class ToolDetailComponent implements OnInit {
  private route = inject(ActivatedRoute);
  private router = inject(Router);
  private apiService = inject(ApiService);

  tool = signal<any>(null);
  loading = signal<boolean>(true);

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      const id = params.get('id');
      if (id) {
        this.fetchTool(id);
      } else {
        this.router.navigate(['/tools-resources']);
      }
    });
  }

  fetchTool(id: string) {
    this.loading.set(true);
    this.apiService.getTool(id).subscribe({
      next: (data) => {
        this.tool.set(data);
        this.loading.set(false);
      },
      error: (err) => {
        console.error('Error fetching tool:', err);
        this.loading.set(false);
        // potentially navigate back or show error
      }
    });
  }

  getMailToLink(item: any): string {
    const subject = `Inquiry about Tool: ${item.title}`;
    const body = `Hello,\n\nI am interested in learning more about the Tool "${item.title}".\n\nPlease provide more information.\n\nBest regards,`;
    return `mailto:sales@kmati.in?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  }
}
