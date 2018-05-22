import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CoursecontainerComponent } from './coursecontainer.component';

describe('CoursecontainerComponent', () => {
  let component: CoursecontainerComponent;
  let fixture: ComponentFixture<CoursecontainerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CoursecontainerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CoursecontainerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
