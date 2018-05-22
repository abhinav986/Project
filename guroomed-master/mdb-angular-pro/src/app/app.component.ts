import { Component } from '@angular/core';
import { ShoppingcartService } from './services/shopcart/shoppingcart.service';
// import { ToastService } from './typescripts/pro/alerts';

@Component({
  selector: 'mdb-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.css']

})

export class AppComponent {

  constructor(private shoppingCartService: ShoppingcartService) {

  }

  ngOnInit() {

    if (localStorage.getItem('cart_key')) {
      var countItem = JSON.parse(localStorage.getItem('cart_key'));
      this.shoppingCartService.cartCounter(countItem.items.length);
    }

    if (localStorage.getItem('user_id')) {
      this.shoppingCartService.getCartItem(localStorage.getItem('user_id')).subscribe(data => {
        this.shoppingCartService.cartCounter(data['count']);
      });
    }
  }

}
