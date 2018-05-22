import { TestBed, inject } from '@angular/core/testing';

import { MycoursesService } from './mycourses.service';

describe('MycoursesService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [MycoursesService]
    });
  });

  it('should be created', inject([MycoursesService], (service: MycoursesService) => {
    expect(service).toBeTruthy();
  }));
});
