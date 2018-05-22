import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InstructorSignUpComponent } from './instructor-sign-up.component';

describe('InstructorSignUpComponent', () => {
  let component: InstructorSignUpComponent;
  let fixture: ComponentFixture<InstructorSignUpComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InstructorSignUpComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InstructorSignUpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
