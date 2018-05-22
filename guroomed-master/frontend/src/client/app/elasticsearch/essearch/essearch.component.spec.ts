import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EssearchComponent } from './essearch.component';

describe('EssearchComponent', () => {
  let component: EssearchComponent;
  let fixture: ComponentFixture<EssearchComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EssearchComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EssearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
