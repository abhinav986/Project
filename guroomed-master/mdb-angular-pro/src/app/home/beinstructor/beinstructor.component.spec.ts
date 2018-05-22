import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BeinstructorComponent } from './beinstructor.component';

describe('BeinstructorComponent', () => {
  let component: BeinstructorComponent;
  let fixture: ComponentFixture<BeinstructorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BeinstructorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BeinstructorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
