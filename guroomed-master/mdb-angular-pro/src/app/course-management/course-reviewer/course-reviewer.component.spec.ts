import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CourseReviewerComponent } from './course-reviewer.component';

describe('CourseReviewerComponent', () => {
  let component: CourseReviewerComponent;
  let fixture: ComponentFixture<CourseReviewerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CourseReviewerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CourseReviewerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
