import { Injectable } from '@angular/core';

export abstract class LocalStorageService {
  public abstract get(): Storage;
}

@Injectable()
export class StorageService extends LocalStorageService {

  public get(): Storage {
    return localStorage;
  }
}
