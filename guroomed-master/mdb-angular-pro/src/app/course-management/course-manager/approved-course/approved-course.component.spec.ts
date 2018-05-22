import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ApprovedCourseComponent } from './approved-course.component';

describe('ApprovedCourseComponent', () => {
  let component: ApprovedCourseComponent;
  let fixture: ComponentFixture<ApprovedCourseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ApprovedCourseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ApprovedCourseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
