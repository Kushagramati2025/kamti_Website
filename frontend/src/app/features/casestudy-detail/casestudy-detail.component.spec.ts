import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CasestudyDetailComponent } from './casestudy-detail.component';

describe('CasestudyDetailComponent', () => {
  let component: CasestudyDetailComponent;
  let fixture: ComponentFixture<CasestudyDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CasestudyDetailComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CasestudyDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
