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

  activeTab = signal<'tools' | 'casestudies'>('tools');
  tools = signal<any[]>([]);
  caseStudies = signal<any[]>([]);

  ngOnInit() {
    this.fetchTools();
    this.fetchCaseStudies();
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

  setActiveTab(tab: 'tools' | 'casestudies') {
    this.activeTab.set(tab);
  }
}
