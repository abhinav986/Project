import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PopularcoursesComponent } from './popularcourses.component';

describe('PopularcoursesComponent', () => {
  let component: PopularcoursesComponent;
  let fixture: ComponentFixture<PopularcoursesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PopularcoursesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PopularcoursesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
