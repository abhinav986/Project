import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CoursePriceCouponsComponent } from './course-price-coupons.component';

describe('CoursePriceCouponsComponent', () => {
  let component: CoursePriceCouponsComponent;
  let fixture: ComponentFixture<CoursePriceCouponsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CoursePriceCouponsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CoursePriceCouponsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
