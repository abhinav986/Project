import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class TransactionService {
  transactionUrl = '/api/paypal/orders/'

  constructor(private http: HttpClient) { }

  getTransactionDetails() {
    return this.http.get(this.transactionUrl + localStorage.getItem('user_id'));
  }
}
