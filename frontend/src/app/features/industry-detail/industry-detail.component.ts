import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-industry-detail',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './industry-detail.component.html',
  styleUrl: './industry-detail.component.css'
})
export class IndustryDetailComponent implements OnInit {
  route = inject(ActivatedRoute);
  apiService = inject(ApiService);
  industry: any = null;
  loading = true;

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      const slug = params.get('slug');
      if (slug) {
        this.loading = true;
        this.apiService.getIndustry(slug).subscribe(data => {
          this.industry = data;
          this.loading = false;
        });
      }
    });
  }
  getImageUrl(path: string | null): string {
    if (!path) return '';
    if (path.startsWith('http')) return path;
    return `http://127.0.0.1:8000${path}`;
  }
}
