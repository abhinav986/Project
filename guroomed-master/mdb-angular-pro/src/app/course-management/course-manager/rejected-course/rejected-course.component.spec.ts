import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RejectedCourseComponent } from './rejected-course.component';

describe('RejectedCourseComponent', () => {
  let component: RejectedCourseComponent;
  let fixture: ComponentFixture<RejectedCourseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RejectedCourseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RejectedCourseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
