import { Component, OnInit, OnDestroy, inject, signal, HostListener } from '@angular/core';
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
export class ToolsResourcesComponent implements OnInit, OnDestroy {
  private apiService = inject(ApiService);

  activeTab = signal<'tools' | 'casestudies' | 'usecases'>('tools');
  activeUseCaseCategory = signal<string>('ALL');
  selectedImage = signal<string | null>(null);

  tools = signal<any[]>([]);
  caseStudies = signal<any[]>([]);
  useCases = signal<any[]>([]);
  computedUseCases = signal<any[]>([]);

  ngOnInit() {
    this.fetchTools();
    this.fetchCaseStudies();
    this.fetchUseCases();
  }

  ngOnDestroy() {
    // Ensure scrolling is restored if component is destroyed while modal is open
    this.closeImageModal();
  }

  @HostListener('document:keydown.escape', ['$event'])
  onKeydownHandler(event: KeyboardEvent) {
    if (this.selectedImage()) {
      this.closeImageModal();
    }
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

  openImageModal(imageUrl: string) {
    this.selectedImage.set(imageUrl);
    // Prevent scrolling when modal is open
    document.body.style.overflow = 'hidden';
  }

  closeImageModal() {
    this.selectedImage.set(null);
    // Restore scrolling
    document.body.style.overflow = 'auto';
  }
}
