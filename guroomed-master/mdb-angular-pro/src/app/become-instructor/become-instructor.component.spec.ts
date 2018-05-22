import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BecomeInstructorComponent } from './become-instructor.component';

describe('BecomeInstructorComponent', () => {
  let component: BecomeInstructorComponent;
  let fixture: ComponentFixture<BecomeInstructorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BecomeInstructorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BecomeInstructorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
