import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CourseCommunicationComponent } from './course-communication.component';

describe('CourseCommunicationComponent', () => {
  let component: CourseCommunicationComponent;
  let fixture: ComponentFixture<CourseCommunicationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CourseCommunicationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CourseCommunicationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
