import { TestBed, inject } from '@angular/core/testing';

import { CourseFilterService } from './course-filter.service';

describe('CourseFilterService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CourseFilterService]
    });
  });

  it('should be created', inject([CourseFilterService], (service: CourseFilterService) => {
    expect(service).toBeTruthy();
  }));
});
