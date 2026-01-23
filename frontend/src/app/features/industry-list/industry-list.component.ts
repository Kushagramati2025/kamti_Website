import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-industry-list',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './industry-list.component.html',
  styleUrl: './industry-list.component.css'
})
export class IndustryListComponent implements OnInit {
  apiService = inject(ApiService);
  industries: any[] = [];
  loading = true;

  ngOnInit() {
    this.apiService.getIndustries().subscribe(data => {
      this.industries = data;
      this.loading = false;
    });
  }
}
