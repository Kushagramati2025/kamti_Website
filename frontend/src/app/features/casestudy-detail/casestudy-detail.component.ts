import { Component, inject, signal, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterModule, Router } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-casestudy-detail',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './casestudy-detail.component.html',
  styleUrl: './casestudy-detail.component.css'
})
export class CasestudyDetailComponent implements OnInit {
  private route = inject(ActivatedRoute);
  private router = inject(Router);
  private apiService = inject(ApiService);

  study = signal<any>(null);
  loading = signal<boolean>(true);

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      const id = params.get('id');
      if (id) {
        this.fetchStudy(id);
      } else {
        this.router.navigate(['/tools-resources']);
      }
    });
  }

  fetchStudy(id: string) {
    this.loading.set(true);
    this.apiService.getCaseStudy(id).subscribe({
      next: (data) => {
        this.study.set(data);
        this.loading.set(false);
      },
      error: (err) => {
        console.error('Error fetching case study:', err);
        this.loading.set(false);
      }
    });
  }

  getMailToLink(item: any): string {
    const subject = `Inquiry about Case Study: ${item.title}`;
    const body = `Hello,\n\nI am interested in learning more about the Case Study "${item.title}".\n\nPlease provide more information.\n\nBest regards,`;
    return `mailto:sales@kmati.in?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  }
}
