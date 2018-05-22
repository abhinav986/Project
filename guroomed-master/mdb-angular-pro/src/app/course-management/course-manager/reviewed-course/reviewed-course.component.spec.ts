import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReviewedCourseComponent } from './reviewed-course.component';

describe('ReviewedCourseComponent', () => {
  let component: ReviewedCourseComponent;
  let fixture: ComponentFixture<ReviewedCourseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReviewedCourseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReviewedCourseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
