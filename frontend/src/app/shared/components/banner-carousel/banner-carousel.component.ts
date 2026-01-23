import { Component, Input, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ApiService } from '../../../core/services/api.service';

@Component({
    selector: 'app-banner-carousel',
    standalone: true,
    imports: [CommonModule, RouterModule],
    template: `
    <div class="relative w-full overflow-hidden group h-[60vh] min-h-[400px] lg:h-[650px]">
        <!-- Loading State -->
        <div *ngIf="loading" class="absolute inset-0 z-50 flex items-center justify-center bg-brand-purple">
            <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-brand-orange"></div>
        </div>

        <!-- Dynamic Background Slideshow -->
        <div class="absolute inset-0 z-0">
             <div *ngFor="let img of backgroundImages; let i = index" 
                 class="absolute inset-0 w-full h-full transition-opacity duration-1000 ease-in-out"
                 [ngClass]="{'opacity-100': i === currentBgIndex, 'opacity-0': i !== currentBgIndex}">
                <img [src]="img" class="w-full h-full object-cover transform scale-105 transition-transform duration-[10000ms] ease-linear"
                     [ngClass]="{'scale-100': i === currentBgIndex}" alt="Background">
                 <!-- Gradient Overlay to ensure text readability -->
                <div class="absolute inset-0 bg-gradient-to-t from-brand-purple/95 via-brand-purple/80 to-brand-purple/60 mix-blend-multiply"></div>
                <div class="absolute inset-0 bg-black/20"></div>
            </div>
        </div>

        <!-- Banner Content (Text) -->
        <div *ngIf="!loading && banners.length > 0" class="absolute inset-0 z-10 flex items-center justify-center">
            <div *ngFor="let banner of banners; let i = index" 
                 class="absolute inset-0 w-full h-full flex items-center justify-center transition-opacity duration-1000"
                 [ngClass]="{'opacity-100 pointer-events-auto': i === currentBannerIndex, 'opacity-0 pointer-events-none': i !== currentBannerIndex}">
                
                <div class="text-center px-4 max-w-5xl mx-auto">
                    <!-- Animated Text -->
                    <h1 class="text-4xl md:text-5xl lg:text-5xl font-extrabold text-white tracking-tight mb-6 opacity-0 shadow-sm"
                        [ngClass]="{'animate-fade-in-up': i === currentBannerIndex}" style="animation-delay: 200ms;">
                        {{ banner.title }}
                    </h1>
                    <p class="text-lg md:text-xl text-gray-100 font-medium mb-10 opacity-0 max-w-3xl mx-auto leading-relaxed shadow-sm"
                       [ngClass]="{'animate-fade-in-up': i === currentBannerIndex}" style="animation-delay: 400ms;">
                        {{ banner.subtitle }}
                    </p>
                    
                    <a *ngIf="banner.link" [routerLink]="banner.link" 
                       class="inline-block px-8 py-4 bg-brand-orange text-white text-lg font-bold uppercase tracking-widest rounded-full hover:bg-white hover:text-brand-orange transition-all duration-300 transform hover:scale-105 shadow-xl opacity-0"
                       [ngClass]="{'animate-fade-in-up': i === currentBannerIndex}" style="animation-delay: 600ms;">
                        Explore
                    </a>
                </div>
            </div>
        </div>
        
        <!-- Fallback Content -->
        <div *ngIf="!loading && banners.length === 0" class="relative z-10 flex items-center justify-center h-full text-white">
             <div class="text-center">
                 <h1 class="text-4xl font-bold mb-4">{{ fallbackTitle }}</h1>
                 <p class="text-gray-200">{{ fallbackSubtitle }}</p>
             </div>
        </div>
    </div>
  `
})
export class BannerCarouselComponent implements OnInit, OnDestroy {
    @Input() pageContext: string = 'HOME';
    @Input() fallbackTitle: string = 'Welcome to KMATI';
    @Input() fallbackSubtitle: string = 'Innovating for the Future';

    banners: any[] = [];
    loading = true;
    currentBannerIndex = 0;
    currentBgIndex = 0;

    // High-quality Unsplash images for the slideshow
    backgroundImages: string[] = [
        'https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80', // Data Visualization
        'https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=1952&q=80', // Global Tech
        'https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-1.2.1&auto=format&fit=crop&w=2002&q=80', // Workplace/Code
        'https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80'  // Circuit/Chip
    ];

    bannerInterval: any;
    bgInterval: any;

    constructor(private apiService: ApiService) { }

    ngOnInit() {
        this.loadBanners();
        this.startBgRotation();
    }

    loadBanners() {
        this.loading = true;
        this.apiService.getBanners(this.pageContext).subscribe({
            next: (data: any) => {
                this.banners = data;
                this.loading = false;
                if (this.banners.length > 1) {
                    this.startBannerRotation();
                }
            },
            error: (err: any) => {
                console.error('Error loading banners:', err);
                this.loading = false;
            }
        });
    }

    startBannerRotation() {
        this.bannerInterval = setInterval(() => {
            if (this.banners.length > 1) {
                this.currentBannerIndex = (this.currentBannerIndex + 1) % this.banners.length;
            }
        }, 6000);
    }

    startBgRotation() {
        this.bgInterval = setInterval(() => {
            this.currentBgIndex = (this.currentBgIndex + 1) % this.backgroundImages.length;
        }, 5000);
    }

    ngOnDestroy() {
        if (this.bannerInterval) clearInterval(this.bannerInterval);
        if (this.bgInterval) clearInterval(this.bgInterval);
    }
}
