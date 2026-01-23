import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-career-detail',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './career-detail.component.html',
  styleUrl: './career-detail.component.css'
})
export class CareerDetailComponent implements OnInit {
  route = inject(ActivatedRoute);
  apiService = inject(ApiService);
  job: any = null;
  loading = true;

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      const id = params.get('id');
      if (id) {
        this.loading = true;
        this.apiService.getCareer(id).subscribe(data => {
          this.job = data;
          this.loading = false;
        });
      }
    });
  }
}
