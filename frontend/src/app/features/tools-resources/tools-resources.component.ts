import { Component, OnInit, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-tools-resources',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './tools-resources.component.html',
  styleUrl: './tools-resources.component.css'
})
export class ToolsResourcesComponent implements OnInit {
  private apiService = inject(ApiService);

  activeTab = signal<'tools' | 'casestudies' | 'usecases'>('tools');
  activeUseCaseCategory = signal<string>('ALL');

  tools = signal<any[]>([]);
  caseStudies = signal<any[]>([]);
  useCases = signal<any[]>([]);
  computedUseCases = signal<any[]>([]);

  ngOnInit() {
    this.fetchTools();
    this.fetchCaseStudies();
    this.fetchUseCases();
  }

  fetchTools() {
    this.apiService.getTools().subscribe({
      next: (data) => this.tools.set(data),
      error: (err) => console.error('Error fetching tools:', err)
    });
  }

  fetchCaseStudies() {
    this.apiService.getCaseStudies().subscribe({
      next: (data) => this.caseStudies.set(data),
      error: (err) => console.error('Error fetching case studies:', err)
    });
  }

  fetchUseCases() {
    this.apiService.getUseCases().subscribe({
      next: (data) => {
        this.useCases.set(data);
        this.filterUseCases();
      },
      error: (err) => console.error('Error fetching use cases:', err)
    });
  }

  setActiveTab(tab: 'tools' | 'casestudies' | 'usecases') {
    this.activeTab.set(tab);
  }

  setUseCaseCategory(category: string) {
    this.activeUseCaseCategory.set(category);
    this.filterUseCases();
  }

  filterUseCases() {
    const category = this.activeUseCaseCategory();
    if (category === 'ALL') {
      this.computedUseCases.set(this.useCases());
    } else {
      this.computedUseCases.set(this.useCases().filter(uc => uc.category === category));
    }
  }
}
