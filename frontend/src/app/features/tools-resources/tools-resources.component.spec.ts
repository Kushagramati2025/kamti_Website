import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ToolsResourcesComponent } from './tools-resources.component';

describe('ToolsResourcesComponent', () => {
  let component: ToolsResourcesComponent;
  let fixture: ComponentFixture<ToolsResourcesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ToolsResourcesComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ToolsResourcesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
