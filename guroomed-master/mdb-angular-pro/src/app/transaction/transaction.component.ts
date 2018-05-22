import { Component, OnInit } from '@angular/core';
import { NavbarService } from 'app/shared/navbarService/navbar.service';
import { TransactionService } from './transaction.service';

@Component({
  selector: 'app-transaction',
  templateUrl: './transaction.component.html',
  styleUrls: ['./transaction.component.scss']
})
export class TransactionComponent implements OnInit {
  transactionRecord;
  constructor(private nav: NavbarService, private transactionService: TransactionService) { }

  ngOnInit() {
    this.nav.show();
    this.transactionDetails();
  }

  transactionDetails() {
    this.transactionService.getTransactionDetails()
      .subscribe(data => {
        this.transactionRecord = data['orders'];
      });
  }
}
