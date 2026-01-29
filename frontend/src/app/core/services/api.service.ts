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

    getPageSections(page?: string, key?: string): Observable<any[]> {
        let url = `${this.apiUrl}/page-sections/`;
        // Basic query param handling (could be more robust)
        if (page || key) {
            url += '?';
            const params = [];
            if (page) params.push(`page=${page}`);
            if (key) params.push(`key=${key}`);
            url += params.join('&');
        }
        return this.http.get<any[]>(url);
    }

    getDepartments(): Observable<any[]> {
        return this.http.get<any[]>(`${this.apiUrl}/departments/`);
    }

    getCareers(departmentId?: number): Observable<any[]> {
        let url = `${this.apiUrl}/careers/`;
        if (departmentId) {
            url += `?department=${departmentId}`;
        }
        return this.http.get<any[]>(url);
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
