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
            { path: '', component: HomeComponent },
            { path: 'services', component: ServicesComponent },
            { path: 'tools-resources', loadComponent: () => import('./features/tools-resources/tools-resources.component').then(m => m.ToolsResourcesComponent) },
            { path: 'industries', component: IndustryListComponent },
            { path: 'industries/:slug', component: IndustryDetailComponent },
            { path: 'careers', component: CareerListComponent },
            { path: 'careers/:id', component: CareerDetailComponent },
            { path: 'blog', component: BlogListComponent },
            { path: 'blog/:slug', component: BlogDetailComponent },
            { path: 'contact', component: ContactComponent },
            { path: 'about', component: AboutComponent },
            { path: 'leadership', component: LeadershipComponent },
            { path: 'partners', component: PartnersComponent },
            { path: 'values', component: ValuesComponent },
            { path: 'vision-mission', component: VisionMissionComponent },
            { path: 'leaders-innovating', component: LeadersInnovatingComponent },
        ]
    },
    { path: '**', redirectTo: '' }
];
