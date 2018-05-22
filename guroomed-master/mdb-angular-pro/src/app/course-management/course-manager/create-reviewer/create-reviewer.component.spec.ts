import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateReviewerComponent } from './create-reviewer.component';

describe('CreateReviewerComponent', () => {
  let component: CreateReviewerComponent;
  let fixture: ComponentFixture<CreateReviewerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateReviewerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateReviewerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
