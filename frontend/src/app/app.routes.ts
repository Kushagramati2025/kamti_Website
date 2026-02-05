import { Routes } from '@angular/router';
import { MainLayoutComponent } from './layout/main-layout/main-layout.component';
import { HomeComponent } from './features/home/home.component';
import { ServicesComponent } from './features/services/services.component';
import { IndustryListComponent } from './features/industry-list/industry-list.component';
import { IndustryDetailComponent } from './features/industry-detail/industry-detail.component';
import { CareerListComponent } from './features/career-list/career-list.component';
import { CareerDetailComponent } from './features/career-detail/career-detail.component';
import { BlogListComponent } from './features/blog-list/blog-list.component';
import { BlogDetailComponent } from './features/blog-detail/blog-detail.component';
import { ContactComponent } from './features/contact/contact.component';
import { AboutComponent } from './features/about/about.component';
import { LeadershipComponent } from './features/leadership/leadership.component';
import { PartnersComponent } from './features/partners/partners.component';
import { ValuesComponent } from './features/values/values.component';
import { VisionMissionComponent } from './features/vision-mission/vision-mission.component';
import { LeadersInnovatingComponent } from './features/leaders-innovating/leaders-innovating.component';

export const routes: Routes = [
    {
        path: '',
        component: MainLayoutComponent,
        children: [
            { path: '', component: HomeComponent, data: { title: 'Home' } },
            { path: 'services', component: ServicesComponent, data: { title: 'Services' } },
            { path: 'tools-resources', loadComponent: () => import('./features/tools-resources/tools-resources.component').then(m => m.ToolsResourcesComponent), data: { title: 'Our Tools' } },
            { path: 'tools/:id', loadComponent: () => import('./features/tool-detail/tool-detail.component').then(m => m.ToolDetailComponent), data: { title: 'Tool Detail' } },
            { path: 'casestudies/:id', loadComponent: () => import('./features/casestudy-detail/casestudy-detail.component').then(m => m.CasestudyDetailComponent), data: { title: 'Case Study' } },
            { path: 'industries', component: IndustryListComponent, data: { title: 'Industries' } },
            { path: 'industries/:slug', component: IndustryDetailComponent, data: { title: 'Industry Solution' } },
            { path: 'careers', component: CareerListComponent, data: { title: 'Careers' } },
            { path: 'careers/:id', component: CareerDetailComponent, data: { title: 'Job Detail' } },
            { path: 'blog', component: BlogListComponent, data: { title: 'Blog' } },
            { path: 'blog/:slug', component: BlogDetailComponent, data: { title: 'Blog Post' } },
            { path: 'contact', component: ContactComponent, data: { title: 'Contact Us' } },
            { path: 'about', component: AboutComponent, data: { title: 'About Us' } },
            { path: 'leadership', component: LeadershipComponent, data: { title: 'Leadership' } },
            { path: 'partners', component: PartnersComponent, data: { title: 'Partners' } },
            { path: 'values', component: ValuesComponent, data: { title: 'Values' } },
            { path: 'vision-mission', component: VisionMissionComponent, data: { title: 'Vision & Mission' } },
            { path: 'leaders-innovating', component: LeadersInnovatingComponent, data: { title: 'Leaders Innovating' } },
        ]
    },
    { path: '**', redirectTo: '' }
];
