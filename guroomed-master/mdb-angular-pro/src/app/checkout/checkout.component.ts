import { Component, OnInit } from '@angular/core';
import { NavbarService } from '../shared/navbarService/navbar.service';
import { CheckoutService } from '../cart/checkout.service';

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.scss']
})
export class CheckoutComponent implements OnInit {
  checkoutData;
  proceed;
  constructor(private nav: NavbarService, private checkoutService: CheckoutService) {
    this.nav.show();
  }

  ngOnInit() {
    this.checkoutService.paypal()
      .subscribe(data => {
        this.checkoutData = data['context'];
        this.proceed = this.checkoutData.params;
      });
  }

}
