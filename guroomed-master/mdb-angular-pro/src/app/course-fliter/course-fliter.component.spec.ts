import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CourseFliterComponent } from './course-fliter.component';

describe('CourseFliterComponent', () => {
  let component: CourseFliterComponent;
  let fixture: ComponentFixture<CourseFliterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CourseFliterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CourseFliterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
