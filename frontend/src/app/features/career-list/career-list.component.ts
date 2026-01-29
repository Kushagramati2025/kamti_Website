import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { ApiService } from '../../core/services/api.service';
import { BannerCarouselComponent } from '../../shared/components/banner-carousel/banner-carousel.component';


@Component({
  selector: 'app-career-list',
  standalone: true,
  imports: [CommonModule, RouterLink, BannerCarouselComponent],
  templateUrl: './career-list.component.html',
  styleUrl: './career-list.component.css'
})
export class CareerListComponent implements OnInit {
  apiService = inject(ApiService);
  jobs: any[] = [];
  departments: any[] = [];
  loading = true;

  // Configurable Section
  sectionTitle = 'Open Positions';
  sectionSubtitle = 'Ready to make an impact? Check out our current openings.';

  selectedDepartmentId: number | null = null;

  ngOnInit() {
    this.loadConfig();
    this.loadDepartments();
    this.loadJobs();
  }

  loadConfig() {
    this.apiService.getPageSections('CAREERS', 'OPEN_POSITIONS').subscribe(sections => {
      if (sections && sections.length > 0) {
        this.sectionTitle = sections[0].title;
        this.sectionSubtitle = sections[0].subtitle;
      }
    });
  }

  loadDepartments() {
    this.apiService.getDepartments().subscribe(data => {
      this.departments = data;
    });
  }

  loadJobs() {
    this.loading = true;
    const deptId = this.selectedDepartmentId ? this.selectedDepartmentId : undefined;
    this.apiService.getCareers(deptId).subscribe(data => {
      this.jobs = data;
      this.loading = false;
    });
  }

  filterByDepartment(deptId: number | null) {
    this.selectedDepartmentId = deptId;
    this.loadJobs();
  }
}
