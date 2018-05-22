import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InfostripComponent } from './infostrip.component';

describe('InfostripComponent', () => {
  let component: InfostripComponent;
  let fixture: ComponentFixture<InfostripComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InfostripComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InfostripComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
