import { TestBed, inject } from '@angular/core/testing';

import { EsserviceService } from './esservice.service';

describe('EsserviceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [EsserviceService]
    });
  });

  it('should be created', inject([EsserviceService], (service: EsserviceService) => {
    expect(service).toBeTruthy();
  }));
});
