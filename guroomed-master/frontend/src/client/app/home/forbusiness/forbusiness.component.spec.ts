import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ForbusinessComponent } from './forbusiness.component';

describe('ForbusinessComponent', () => {
  let component: ForbusinessComponent;
  let fixture: ComponentFixture<ForbusinessComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ForbusinessComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ForbusinessComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
