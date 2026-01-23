import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { ApiService } from '../../core/services/api.service';
import { BannerCarouselComponent } from '../../shared/components/banner-carousel/banner-carousel.component';

@Component({
  selector: 'app-contact',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterLink, RouterLinkActive, BannerCarouselComponent],
  templateUrl: './contact.component.html',
  styleUrl: './contact.component.css'
})
export class ContactComponent {
  fb = inject(FormBuilder);
  apiService = inject(ApiService);

  contactForm: FormGroup = this.fb.group({
    name: ['', Validators.required],
    email: ['', [Validators.required, Validators.email]],
    phone: [''],
    subject: [''],
    message: ['', Validators.required],
    attachment: [null]
  });

  submitting = false;
  successMessage = '';
  errorMessage = '';

  onFileChange(event: any) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.contactForm.patchValue({
        attachment: file
      });
    }
  }

  onSubmit() {
    if (this.contactForm.invalid) {
      return;
    }

    this.submitting = true;
    this.successMessage = '';
    this.errorMessage = '';

    const formData = new FormData();
    formData.append('name', this.contactForm.get('name')?.value);
    formData.append('email', this.contactForm.get('email')?.value);
    formData.append('phone', this.contactForm.get('phone')?.value || '');
    formData.append('subject', this.contactForm.get('subject')?.value || '');
    formData.append('message', this.contactForm.get('message')?.value);

    if (this.contactForm.get('attachment')?.value) {
      formData.append('attachment', this.contactForm.get('attachment')?.value);
    }

    this.apiService.contact(formData).subscribe({
      next: (response) => {
        this.submitting = false;
        this.successMessage = 'Thank you for contacting us! We will get back to you soon.';
        this.contactForm.reset();
      },
      error: (error) => {
        this.submitting = false;
        this.errorMessage = 'Something went wrong. Please try again later.';
        console.error('Contact error:', error);
      }
    });
  }
}
