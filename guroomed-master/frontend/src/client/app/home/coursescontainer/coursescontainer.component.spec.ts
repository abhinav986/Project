import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CoursescontainerComponent } from './coursescontainer.component';

describe('CoursescontainerComponent', () => {
  let component: CoursescontainerComponent;
  let fixture: ComponentFixture<CoursescontainerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CoursescontainerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CoursescontainerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
