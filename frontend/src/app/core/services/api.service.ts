import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class ApiService {
    private http = inject(HttpClient);
    private apiUrl = 'http://127.0.0.1:8000/api';

    getBanners(page: string = 'HOME'): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/banners/?page=${page}`);
    }

    getServices(): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/services/`);
    }

    getIndustries(): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/industries/`);
    }

    getIndustry(slug: string): Observable<any> {
        return this.http.get<any>(`${this.apiUrl}/industries/${slug}/`);
    }

    getCareers(): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/careers/`);
    }

    getCareer(id: string): Observable<any> {
        return this.http.get<any>(`${this.apiUrl}/careers/${id}/`);
    }

    getBlogPosts(): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/blog/`);
    }

    getBlogPost(slug: string): Observable<any> {
        return this.http.get<any>(`${this.apiUrl}/blog/${slug}/`);
    }

    getLeadership(): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/leadership/`);
    }

    getPartners(): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/partners/`);
    }

    getValues(): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/values/`);
    }

    getVisionMission(): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/vision-mission/`);
    }

    getTools(): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/tools/`);
    }

    getCaseStudies(): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/case-studies/`);
    }

    contact(data: any): Observable<any> {
        return this.http.post(`${this.apiUrl}/contact/`, data);
    }
}
