import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class CheckoutService {
  paypalUrl = '/api/paypal/checkout';
  constructor(private http: HttpClient) { }

  paypal() {
    return this.http.get(this.paypalUrl);
  }
}
